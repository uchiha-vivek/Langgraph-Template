from src.graph.workflow import build_graph

def main():
    workflow = build_graph()
    print("🤖 Assistant: Hello! Ask me about the weather or the news. Type 'exit' to quit.")

    while True:
        user_input = input("👤 You: ")
        if user_input.strip().lower() == "exit":
            print("🤖 Assistant: Goodbye!")
            break

        result = workflow.invoke({"user_input": user_input})
        print(f"🛠️ Tool Invoked: {result.get('invoked_tool')}")
        print(f"🤖 Assistant: {result['result']}")

if __name__ == "__main__":
    main()