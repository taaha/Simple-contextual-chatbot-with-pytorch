{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"name":"python","version":"3.7.12","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"import random\nimport json\n\nimport torch\n\nfrom model import NeuralNet\nfrom nltk_utils import bag_of_words, tokenize\n\ndevice = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n\nwith open('/kaggle/input/intent-for-chatbot/intents.json', 'r') as json_data:\n    intents = json.load(json_data)\n\nFILE = \"/kaggle/input/chatbot-model/data.pth\"\ndata = torch.load(FILE)\n\ninput_size = data[\"input_size\"]\nhidden_size = data[\"hidden_size\"]\noutput_size = data[\"output_size\"]\nall_words = data['all_words']\ntags = data['tags']\nmodel_state = data[\"model_state\"]\n\nmodel = NeuralNet(input_size, hidden_size, output_size).to(device)\nmodel.load_state_dict(model_state)\nmodel.eval()\n\nbot_name = \"Sam\"\nprint(\"Let's chat! (type 'quit' to exit)\")\nwhile True:\n    # sentence = \"do you use credit cards?\"\n    sentence = input(\"You: \")\n    if sentence == \"quit\":\n        break\n\n    sentence = tokenize(sentence)\n    X = bag_of_words(sentence, all_words)\n    X = X.reshape(1, X.shape[0])\n    X = torch.from_numpy(X).to(device)\n\n    output = model(X)\n    _, predicted = torch.max(output, dim=1)\n\n    tag = tags[predicted.item()]\n\n    probs = torch.softmax(output, dim=1)\n    prob = probs[0][predicted.item()]\n    if prob.item() > 0.75:\n        for intent in intents['intents']:\n            if tag == intent[\"tag\"]:\n                print(f\"{bot_name}: {random.choice(intent['responses'])}\")\n    else:\n        print(f\"{bot_name}: I do not understand...\")","metadata":{"_uuid":"8f2839f25d086af736a60e9eeb907d3b93b6e0e5","_cell_guid":"b1076dfc-b9ad-4769-8c92-a6c4dae69d19","execution":{"iopub.status.busy":"2023-02-17T18:09:30.587291Z","iopub.execute_input":"2023-02-17T18:09:30.587705Z","iopub.status.idle":"2023-02-17T18:09:45.493991Z","shell.execute_reply.started":"2023-02-17T18:09:30.587670Z","shell.execute_reply":"2023-02-17T18:09:45.492403Z"},"trusted":true},"execution_count":2,"outputs":[{"name":"stdout","text":"Let's chat! (type 'quit' to exit)\n","output_type":"stream"},{"traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)","\u001b[0;32m/tmp/ipykernel_23/1269000011.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m     \u001b[0;31m# sentence = \"do you use credit cards?\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 32\u001b[0;31m     \u001b[0msentence\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"You: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     33\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0msentence\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"quit\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     34\u001b[0m         \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/opt/conda/lib/python3.7/site-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1180\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_parent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1181\u001b[0;31m             \u001b[0mpassword\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1182\u001b[0m         )\n\u001b[1;32m   1183\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;32m/opt/conda/lib/python3.7/site-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"],"ename":"KeyboardInterrupt","evalue":"Interrupted by user","output_type":"error"}]}]}