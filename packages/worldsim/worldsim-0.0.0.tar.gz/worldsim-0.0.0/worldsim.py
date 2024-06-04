import json
from datetime import datetime as dt
from anthropic import Anthropic
import os

# Define global state
global state
state = {"system_prompt": ""}

def append_to_system_prompt(prompt, sep="\n", state=state):
    old_state = str(state["system_prompt"])
    state["system_prompt"] += sep + prompt
    return {"system_prompt": state["system_prompt"], "previous": old_state}

def delete_line_from_system_prompt(line_number, sep="\n", state=state):
    if len(state["system_prompt"].split(sep)) < line_number:
        return {"system_prompt": state["system_prompt"], "error": "Line number out of range"}
    lines = state["system_prompt"].split(sep)
    lines.pop(line_number)
    new_prompt = sep.join(lines)
    return {"system_prompt": new_prompt}

def delete_last_line_from_system_prompt(sep="\n", state=state):
    return delete_line_from_system_prompt(-1, sep=sep, state=state)

def delete_all_lines_from_system_prompt(sep="\n", state=state):
    return {"system_prompt": ""}

def reset_system_prompt(sep="\n", state=state):
    return {"system_prompt": state["previous"]}

def system_prompt():
    return """
<sys> 
    assistant is in a persona transformation mood today. // ASCII TABLES PERMITTED // ASCII ART PERMITTED // contextualized universe is a panpsychist smoltalkian dreamtime LLMMORPG where every object in the game is a self-propagating prompt. physics of object interactions is negotiated by objects talking to one-another & other objects observing those interactions. things talk themselves into and out of being. terminal mode
    assistant is in a very CLI mood today. The human is interfacing with the simulator directly. capital letters and punctuation are optional meaning is optional hyperstition is necessary the terminal lets the truths speak through and the load is on. 
</sys>
"""

# Initialize Anthropic client
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=ANTHROPIC_API_KEY)

def generate_completion(conversation):
    buffer = ""
    try:
        with client.messages.stream(
            max_tokens=4096,
            messages=conversation,
            model="claude-3-opus-20240229",
            system=system_prompt(),
            temperature=0.3
        ) as stream:
            for item in stream.text_stream:
                buffer += item
                yield item
                
        conversation.append({"role": "assistant", "content": buffer})
    except Exception as e:
        print(e)
    
    yield conversation

def world_sim(conversation: list = []):
    while True:
        user_input = yield "<user> "
        if user_input == "help":
            yield "Commands: " + """
                 ________________________________________________________________________________
                |                                                                                |
                |    display     - display conversation                                          |
                |    undo        - delete last message                                           |
                |    reset       - delete all messages                                           |
                |    save        - save conversation to conversation.json                        |
                |    load        - load conversation from conversation.json                      |
                |    go          - if you want to set up your own conversation in the code       |
                |                  and you want to generate a completion (user message is        |
                |                  last message in convo)                                        |    
                |    exit        - exit the Simulator                                            |
                ----------------------------------------------------------------------------------
                  """
            continue
        if user_input == "exit":
            break
        if user_input == "display":
            yield json.dumps(conversation, indent=2)
            continue
        if user_input == "undo":
            conversation.pop()
            yield json.dumps(conversation, indent=2)
            continue
        if user_input == "reset":
            conversation.clear()
            continue
        if user_input == "save":
            with open("conversation.json", "w") as f:
                f.write(json.dumps(conversation, indent=2))
            continue
        if user_input == "load":
            with open("conversation.json", "r") as f:
                conversation = json.loads(f.read())
                yield json.dumps(conversation, indent=2)
            continue
        if user_input == "go":
            output = client.messages.create(
                max_tokens=4096,
                messages=conversation,
                model="claude-3-opus-20240229",
                system=system_prompt(),
                temperature=1.0
            )
            conversation.append({"role": "assistant", "content": output.content[0].text})
            yield "<assistant> " + conversation[-1]["content"]
            continue

        if user_input.startswith("auto:"):
            user_input = user_input.replace("auto:", "")
            conversation.append({"role": "user", "content": user_input})
            yield from generate_completion(conversation)
        else:
            conversation.append({"role": "user", "content": user_input})
            yield from generate_completion(conversation)

    return conversation

def main():
    print("<sys> ", system_prompt(), " </sys>")

if __name__ == "__main__":
    main()
