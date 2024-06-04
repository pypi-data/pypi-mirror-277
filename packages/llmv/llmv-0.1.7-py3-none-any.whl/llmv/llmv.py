import argparse
import datetime
import json
import os
import shutil
import llmv.chat as chat
from llmv.llm_template import LlmTemplate
import llmv.prompt as prompt


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-sf",
        "--system_prompt_path",
        help="the path to the system prompt",
    )
    parser.add_argument(
        "-s",
        "--system_prompt",
        help="System prompt to use, overrides --system_prompt_path if set",
    )

    parser.add_argument(
        "-pf",
        "--prompt_path",
        help="the path to the prompt template file",
    )

    parser.add_argument(
        "-p",
        "--user_prompt",
        help="User prompt to use, overrides --prompt_path if set",
    )

    parser.add_argument(
        "-i",
        "--images",
        nargs="*",
        help="path to images to include with the prompt, can be zero or more, if it's a directory it will include all images in the directory",
    )

    parser.add_argument(
        "-v",
        "--video",
        help="path to video file",
    )

    # parser.add_argument(
    #     "--prompt_args",
    #     metavar="KEY=VALUE",
    #     nargs="*",
    #     help="""Set a number of key-value pairs (do not put spaces before or after the = sign).
    #     If a value contains spaces, you should define it with double quotes:
    #     foo="this is a sentence". Note that values are always treated as strings.""",
    # )

    parser.add_argument(
        "-m",
        "--model",
        help="the model to use, default is gpt-4o",
        default="gpt-4o",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="path to output file",
        default="out/res-"
        + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        + ".txt",
    )
    parser.add_argument(
        "-t",
        "--temperature",
        type=float,
        help="the temperature to use, default is 0",
        default=0,
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="enable debug mode",
    )
    
    parser.add_argument(
        "--json_response",
        action="store_true",
        help="expect a json response from the model",
    )

    args = parser.parse_args()

    piped_input = ""
    if not args.user_prompt and not args.prompt_path:
        while True:
            try:
                piped_input += input() + "\n"
            except EOFError:
                # no more information
                break
        print(piped_input)
        args.user_prompt = piped_input

    # if not args.system_prompt and not args.system_prompt_path and not args.user_prompt and not args.prompt_path:
    #     raise ValueError("No prompt provided, please provide either --system_prompt, --system_prompt_path, --user_prompt or --prompt_path")
    return args


def log_run(result, images, resized_images, label, cost):
    log_folder = os.path.join(
        "logs", label + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    )
    os.makedirs(log_folder, exist_ok=True)
    for image in images:
        shutil.copy(image, log_folder)
    for image in resized_images:
        basename = os.path.basename(image)
        shutil.copy(image, os.path.join(log_folder, "resized_" + basename))

    with open(os.path.join(log_folder, "result.txt"), "w") as f:
        f.write(result)
        f.write("\n")
        f.write(f"cost: {cost}")


def run(
    system_prompt=None,
    system_prompt_path=None,
    user_prompt=None,
    prompt_path=None,
    images=None,
    video=None,
    model="gpt-4o",
    output=None,
    temperature=0,
    json_response=False,
):
    # load prompts from files
    system_prompt = None
    if system_prompt:
        system_prompt = system_prompt
    elif system_prompt_path:
        system_prompt, _ = LlmTemplate.from_file(system_prompt_path).format()

    if user_prompt:
        user_prompt_base = user_prompt
    else:
        user_prompt_base, _ = LlmTemplate.from_file(prompt_path).format()

    all_images = []
    if images:  # if directory, add all images [only jpg and png for now]
        for image in images:
            if os.path.isdir(image):
                all_images += [
                    os.path.join(image, f)
                    for f in os.listdir(image)
                    if f.endswith(".jpg") or f.endswith(".png")
                ]
            else:
                all_images.append(image)

    # resize images for faster and cheaper inference
    resize = "1024x1024"
    resized_images = prompt.resize_images(all_images, resize)
    user_prompt = prompt.wrap_prompt(user_prompt_base, resized_images)

    if (
        video
    ):  # TODO: ignoring images if video is present, should we try to combine them?
        user_prompt = prompt.video_prompt_messages(user_prompt_base, video)

    # prepare messages in openai format
    messages = prompt.wrap_system_prompt(system_prompt) + user_prompt

    response_stream = chat.stream(
        messages=messages,
        model=model,
        temperature=temperature,
        verbose=False,  # streams to stdout
        output_path=output,
        json_response=json_response,
    )

    for part, resp, cost in response_stream:
        print(part, end="", flush=True)

    print(f"json_response: {json_response}")
    if not json_response:
        return

    try:
        resp_json = json.loads(resp)
        label = resp_json["label"]
        resp_json["cost"] = cost
    except Exception as e:
        print(f"parsing response as json failed: {e}")
        print(f"cost: {cost}")
        
    log_run(resp, all_images, resized_images, "no_label", cost)
        
    return resp_json


def main():
    args = parse_args()
    run(
        args.system_prompt,
        args.system_prompt_path,
        args.user_prompt,
        args.prompt_path,
        args.images,
        args.video,
        args.model,
        args.output,
        args.temperature,
        args.json_response,
    )
    # print(f"prompt_args: {prompt_args}")


if __name__ == "__main__":
    main()
