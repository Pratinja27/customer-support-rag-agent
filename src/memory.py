from langgraph.checkpoint.sqlite import SqliteSaver

memory = SqliteSaver.from_conn_string("chat_memory.db").__enter__()