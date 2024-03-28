# Mojo implementation of agents
import os
import memory
from prompts import ACTION_PROMPTS, 

fn main(question):
    answer_dict = prompt_core_llm(question, memory)
    update_memory()
    if answer_dict[tools]:
        execute_tool()
        update_memory()
    if answer_dict[planner]:
        questions = execute_planner()
        update_memory()
    if no_new_questions and no tool request:
        return generate_final_answer(memory)


def config():