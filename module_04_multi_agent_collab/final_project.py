import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# --- Data Models ---
class Outline(BaseModel):
    sections: List[str] = Field(description="List of section titles for the blog post.")

class Research(BaseModel):
    notes: str = Field(description="Research notes for the section.")

# --- Agents ---

# 1. Planner
planner_parser = JsonOutputParser(pydantic_object=Outline)
planner_prompt = ChatPromptTemplate.from_template("""
You are a Content Strategist. Create a 3-section outline for a blog post about: {topic}.
Return JSON with a 'sections' key.
{format_instructions}
""")
planner_chain = planner_prompt | llm | planner_parser

# 2. Researcher
researcher_prompt = ChatPromptTemplate.from_template("""
You are a Researcher. Provide 3 bullet points of key information for the section: {section_title}.
Topic: {topic}
""")
researcher_chain = researcher_prompt | llm

# 3. Writer
writer_prompt = ChatPromptTemplate.from_template("""
You are a Blog Writer. Write a engaging paragraph for the section '{section_title}' based on these notes:
{notes}
""")
writer_chain = writer_prompt | llm

# 4. Editor
editor_prompt = ChatPromptTemplate.from_template("""
You are an Editor. Review the following blog post. 
Fix any grammar issues and ensure a consistent, professional tone.
Return the polished markdown.

Draft:
{draft}
""")
editor_chain = editor_prompt | llm

# --- The Workflow ---

def run_content_pipeline(topic):
    print(f"--- Starting Pipeline: {topic} ---")
    
    # Step 1: Plan
    print("1. Planner: Creating outline...")
    outline = planner_chain.invoke({
        "topic": topic,
        "format_instructions": planner_parser.get_format_instructions()
    })
    sections = outline["sections"]
    print(f"Outline: {sections}")
    
    full_draft = f"# {topic}\n\n"
    
    # Step 2 & 3: Research & Write (Loop)
    for section in sections:
        print(f"\nProcessing Section: {section}")
        
        # Research
        print("  - Researcher: Gathering info...")
        notes = researcher_chain.invoke({"section_title": section, "topic": topic}).content
        
        # Write
        print("  - Writer: Drafting content...")
        content = writer_chain.invoke({"section_title": section, "notes": notes}).content
        
        full_draft += f"## {section}\n{content}\n\n"
    
    print("\n--- Draft Complete ---")
    
    # Step 4: Edit
    print("4. Editor: Polishing...")
    final_post = editor_chain.invoke({"draft": full_draft}).content
    
    print(f"\n=== FINAL POST ===\n{final_post}")
    
    # Save to file
    filename = f"{topic.replace(' ', '_').lower()}.md"
    with open(filename, "w") as f:
        f.write(final_post)
    print(f"\nSaved to {filename}")

if __name__ == "__main__":
    run_content_pipeline("The Benefits of Urban Gardening")
