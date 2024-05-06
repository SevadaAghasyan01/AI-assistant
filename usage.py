from utils import store_docs, get_response
from dotenv import load_dotenv

load_dotenv()

store_docs("http://www.accel.com/")


# Get response

response = get_response("What is the VC name, contacts, industries that they invest in, investment rounds that they participate/lead.")
print("Answer:", response)