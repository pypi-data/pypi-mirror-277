#coding=utf-8

from XEdu.hub import Workflow as wf
import cv2
import numpy as np 


def pose_infer_demo():
    # a = time.time()
    img = 'pose2.jpg' # 指定进行推理的图片路径
    img = cv2.imread(img)

    det = wf(task='det_body_L')#,checkpoint="checkpoints/bodydetect_l.onnx")
    pose = wf(task='pose_body_l')# ,checkpoint="rtmpose-l-19c9d1.onnx")# "rtmpose-m-80e511.onnx") # 实例化mmpose模型
    
    import time
    a = time.time()
    bbox = det.inference(data=img)
    print(time.time()-a)
    for i in bbox:
        result,img = pose.inference(data=img,img_type='cv2',bbox=i) # 在CPU上进行推理
        pose.show(img)
    # cv2.imshow("img",img)
    # cv2.waitKey(0)
    # pose.save(img,"pimg_ou.png")
    
    result = pose.format_output(lang="zh")
    # print(result)

def video_infer_demo():
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("gyt.mp4")
    
    pose = wf(task='pose_body')
    det = wf(task='det_body')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        bboxs = det.inference(data=frame,thr=0.3) # 在CPU上进行推理
        img = frame
        for i in bboxs:
            keypoints,img =pose.inference(data=img,img_type='cv2',bbox=i) # 在CPU上进行推理
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    cap.release()
    cv2.destroyAllWindows()

def det_infer_demo():
    # a = time.time()
    from XEdu.hub import Workflow as wf
    img = 'hand1.jpeg' # 指定进行推理的图片路径

    det = wf(task='det_hand',checkpoint='det_fire.onnx')

    bboxs,im_ou = det.inference(data=img,img_type='pil',show=False) # 在CPU上进行推理
    # print(bboxs)
    # det.save(im_ou,"im_ou_d.jpg")

    det.format_output(lang="zh")
    # print(result)

def hand_video_demo():
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("pose.mp4")

    pose = wf(task='pose_hand21')# ,checkpoint="rtmpose-m-80e511.onnx") # 实例化pose模型

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        keypoints,img =pose.inference(data=frame,img_type='cv2') # 在CPU上进行推理
        
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    cap.release()
    cv2.destroyAllWindows()

def coco_det_demo():
    img = 'cat.jpg' # 指定进行推理的图片路径
    det = wf(task='det_coco_l')#,checkpoint="checkpoints/cocodetect_l.onnx") # 实例化mmpose模型

    result,img = det.inference(data=img,img_type='pil',thr=0.3) # 在CPU上进行推理
    det.show(img)
    det.save(img,"pimg_ou.png")
    
    # re = det.format_output(lang="zh")

def face_det_demo():
    img = 'banniang.jpg' # 指定进行推理的图片路径
    # img = 'face2.jpeg' # 指定进行推理的图片路径

    det = wf(task='det_face' )
    face = wf(task="pose_face")

    result,img = det.inference(data=img,img_type='cv2',scaleFactor=1.4,minNeighbors=8) # 在CPU上进行推理
    re =  det.format_output(lang="zh")

    det.show(img)
    # det.save(img,"banniang1.jpg")
    # for i in result:
    #     ky,img = face.inference(data=img, img_type="cv2",bbox=i)#,erase=False)
    #     face.show(img)
    

def ocr_demo():
    img = 'cat4.jpg' # 指定进行推理的图片路径
    ocr = wf(task='ocr1' )#,checkpoint="rtmdet-coco.onnx") # 实例化mmpose模型

    result,img = ocr.inference(data=img,img_type='pil',show=True) # 在CPU上进行推理
    print(result)
    ocr.show(img)
    ocr.save(img,"img_ou.png")
    
    re = ocr.format_output(lang="zh")

def mmedu_demo():
    mm = wf(task='mmedu',checkpoint="det_fire.onnx")
    result, img = mm.inference(data='fire.jpg',img_type='pil',thr=0.6)
    # mm.show(img)
    # print(result)
    re = mm.format_output(lang="zh")

    # mm = wf(task='mmedu',checkpoint="convert_model.onnx")
    # result, img = mm.inference(data='fire.jpg',img_type='pil',thr=0.6)
    # # mm.show(img)
    # # print(result)
    # re = mm.format_output(lang="zh")

def basenn_demo():
    nn = wf(task='basenn',checkpoint="checkpoints/basenn.onnx") # iris act 
    result,img = nn.inference(data='6.jpg',img_type='cv2')
    re = nn.format_output(lang="zh")
    nn.show(img)

def hand_det_demo():
    img = 'hand4.jpeg' # 指定进行推理的图片路径
    det = wf(task='det_hand') # 实例化mmpose模型
    hand = wf(task='pose_hand')

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        result,img = det.inference(data=frame,img_type='cv2',thr=0.3) # 在CPU上进行推理
        for i in result:
            ky, img = hand.inference(data=img, img_type='cv2',bbox=i)
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
    cap.release()
    cv2.destroyAllWindows()
    # det.save(img,"pimg_ou.png")
    # re = det.format_output(lang="zh")

def custom_demo():
    def pre(path):
        img = cv2.imread(path) 
        img = img.astype(np.float32)
        img = np.expand_dims(img,0) # 增加batch维
        img = np.transpose(img, (0,3,1,2)) # [batch,channel,width,height]
        return img
    
    def post(res,data):
        
        idx = np.argmax(res[0])
        # print(xxx)
        return idx, res[0][0][idx]

    img_path = "ele.jpg"
    mm = wf(task='custom',checkpoint="mobileone-s3-46652f.onnx") # iris act 
    result = mm.inference(data=img_path,preprocess=pre,postprocess=post)
    print(result)

def cls_demo():
    cls = wf(task='cls_imagenet')#checkpoint="mobileone-s3-46652f.onnx") # iris act 
    img = cv2.imread('ele.jpg')
    result,img = cls.inference(data="ele.jpg",img_type="pil")
    cls.show(img)
    # print(result)
    re = cls.format_output(lang="zh")

def baseml_demo():
    ml = wf(task='baseml',checkpoint="baseml_ckpt.pkl") # iris act 
    # result = ml.inference(data=[[1,0.5,-1,0]])
    # result = ml.inference(data=[1,0.5,-1,0])
    result = ml.inference(data=np.array([[0.5,0,1,1]]))


    re = ml.format_output(lang="zh")

def sup_demo():
    from transformers import AutoTokenizer
    from onnxruntime import InferenceSession
    import numpy as np

    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    session = InferenceSession("all-MiniLM-L6-v2/model.onnx")
    # ONNX Runtime expects NumPy arrays as input
    inputs1 = tokenizer("hi", return_tensors="np")
    inputs2 = tokenizer("hello hi", return_tensors='np')
    print("inputs",inputs1,inputs2)
    vec1 = np.squeeze(session.run(output_names=["last_hidden_state"], input_feed=dict(inputs1))[0].reshape(1,-1))
    vec2 = np.squeeze(session.run(output_names=["last_hidden_state"], input_feed=dict(inputs2))[0].reshape(1,-1))
    print("outputs",vec1[:10],vec2[:10])

    cos_sim = vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    print(cos_sim)

def style_demo():
    for i in range(5):
        style = wf(task='gen_style' ,style='mosaic') # iris act 
        result = style.inference(data="ele.jpg" ,img_type='cv2')
        style.show(result)
        style.save(result,"ele_{}.jpg".format(i))
    # # 打开摄像头，实时风格迁移
    # cap = cv2.VideoCapture(0)
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #     style = random.choice(styles)
    #     result,img = style.inference(data=frame,img_type='cv2')
    #     cv2.imshow('video', img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

def qa_demo():
    qa = wf(task='nlp_qa')# ,checkpoint="checkpoints/bertsquad-8s.onnx")  # /home/user/下载/chatgpt_项目/bertsquad-12-int8.onnx
    # qa = wf(task='nlp_qa',checkpoint="/home/user/下载/chatgpt_项目/bertsquad-12-int8.onnx")
    # 整理以下字符串
    context_glm = """In life, we often encounter challenges that make us question our abilities and motivate us to give up. However, the secret to success lies in persistence. Only by persevering through difficult times can we unlock our true potential and achieve our goals.
Michael Jordan, one of the greatest basketball players of all time, was once cut from his high school team. Instead of giving up, he practiced relentlessly and eventually earned a spot on the team. His perseverance and determination are what made him a legendary athlete.
Another example of persistence is Elon Musk, the CEO of SpaceX and Tesla. He has faced countless setbacks in his entrepreneurial ventures, but he hasn't let them stop him. His vision for the future and relentless pursuit of innovation have made him a global sensation.
In life, we will all face obstacles. It's how we respond to these challenges that defines us. Instead of surrendering to defeat, let's embrace the power of persistence and strive for greatness. Remember, success is not a destination but a journey, and the only way to achieve it is to keep moving forward.
"""
    q11 = "Who is Michael Jordan?"
    q22 = "Who is Elon Musk?"
    context = "In its early years, the new convention center failed to meet attendance and revenue expectations.[12] By 2002, many Silicon Valley businesses were choosing the much larger Moscone Center in San Francisco over the San Jose Convention Center due to the latter's limited space. A ballot measure to finance an expansion via a hotel tax failed to reach the required two-thirds majority to pass. In June 2005, Team San Jose built the South Hall, a $6.77 million, blue and white tent, adding 80,000 square feet (7,400 m2) of exhibit space"
    q1 = "By what year many Silicon Valley businesses were choosing the Moscone Center?"
    q2 = "how may votes did the ballot measure need?"
    q3 = "how many square feet did the South Hall add?"
    qa.load_context(context)
    result = qa.inference(data=q11, context=context_glm)
    result = qa.inference(data=q2)
    result = qa.inference(data=q22, context=context_glm)
    result = qa.inference(data=q3)

    print(result)
    res = qa.format_output(lang="en",show_context=False)
    # result, r = qa.inference(data=q4)
    # print(result)

def sim():
    from onnxsim import simplify
    import onnx
    model = onnx.load("udnie-9.onnx")
    model,_ = simplify(model)
    onnx.save(model, "gen_style_udnie.onnx")

def drive_demo():
    from XEdu.hub import Workflow as wf
    drp = wf(task='drive_perception')
    # result = drp.inference(data="demo.jpg")

    result,image = drp.inference(data="cat1.jpg",img_type='pil')
    drp.format_output(lang="zh",isprint=False)

    drp.show(image)
    # drp.save(image,"demo_ou.jpg")

def embedding_demo():
    # 导入依赖库
    from XEdu.hub import Workflow as wf
    from XEdu.utils import get_similarity,visualize_similarity,visualize_probability
    # 实例化图像嵌入模型
    img_emb = wf(task='embedding_image')
    # 实例化文本嵌入模型
    text_emb = wf(task='embedding_text')
    images = ["cat.png","cat1.jpg","cat2.jpg","cat3.jpg","ele.jpg","dog.jpg"]
    texts_zh = ["猫", "狗"]
    texts_en = ["cat", "dog","room","elephant"]

    # image_embeddings = img_emb.inference(data=images)
    # text_zh_embeddings = text_emb.inference(data=texts_zh)
    text_en_embeddings = text_emb.inference(data=texts_en)

    # # 图像 - 文本相似度
    # logits = get_similarity(image_embeddings,text_en_embeddings,use_softmax=False)
    # visualize_similarity(logits, images, texts_en,figsize=(10,20),)
    # visualize_probability(logits, images, texts_en,topk=6,figsize=(10,10))  

    # 文本 - 文本相似度
    logits = get_similarity(text_en_embeddings,text_en_embeddings ,method='cosine',use_softmax=False)
    visualize_similarity(logits, texts_en, texts_en)

    # # 文本 - 图像相似度
    # logits = get_similarity(text_en_embeddings,image_embeddings,method='cosine',use_softmax=False)
    # visualize_similarity(logits, texts_en, images)

    # 图像 - 图像相似度
    # logits = get_similarity(image_embeddings,images_embeddings,method='cosine',use_softmax=False)
    # visualize_similarity(logits, images, imagess)

    print("cosine", logits)


def openvino_demo():
    import openvino as ov 
    from openvino.runtime import Core
    ie = Core()
    devices = ie.available_devices

    for device in devices:
        device_name = ie.get_property(device,'FULL_DEVICE_NAME')
        print(f'{device}:{device_name}')

    from openvino.runtime import Core

    ie =  Core()
    model_xml = './checkpoints/body17.onnx'

    model  = ie.read_model(model=model_xml)
    compiled_model = ie.compile_model(model=model,device_name='CPU')


    input_layer = compiled_model.input(0)
    output_layer = compiled_model.output(0)

    import cv2
    import numpy as np

    image_filename = "pose1.jpg"
    image = cv2.imread(image_filename)
    image.shape

    # N,C,H,W = batch size, number of channels, height, width.
    N, C, H, W = input_layer.shape
    # OpenCV resize expects the destination size as (width, height).
    resized_image = cv2.resize(src=image, dsize=(W, H))
    resized_image.shape

    input_data = np.expand_dims(np.transpose(resized_image, (2, 0, 1)), 0).astype(np.float32)
    input_data.shape


    # for single input models only
    result = compiled_model(input_data)[output_layer]

    # for multiple inputs in a list
    result = compiled_model([input_data])[output_layer]

    # or using a dictionary, where the key is input tensor name or index
    result = compiled_model({input_layer.any_name: input_data})[output_layer]

    print(result)

def openvino_demo():
    import openvino as ov 
    from openvino.runtime import Core

    import cv2
    import numpy as np

    ie =  Core()
    model_xml = './checkpoints/body17.onnx'

    model  = ie.read_model(model=model_xml)
    compiled_model = ie.compile_model(model=model,device_name='CPU')


    input_layer = compiled_model.input(0)
    output_layer = compiled_model.output(0)

    image_filename = "pose1.jpg"
    image = cv2.imread(image_filename)

    # N,C,H,W = batch size, number of channels, height, width.
    N, C, H, W = input_layer.shape
    resized_image = cv2.resize(src=image, dsize=(W, H))

    input_data = np.expand_dims(np.transpose(resized_image, (2, 0, 1)), 0).astype(np.float32)


    # for single input models only
    result = compiled_model(input_data)[output_layer]

    print(result)

def color_demo():
    from XEdu.hub import Workflow as wf
    color = wf(task='gen_color',download_path='new_download')# ,checkpoint='/home/user/下载/colorization-master/colorizer_siggraph17.onnx')
    img = cv2.imread('/home/user/下载/colorization-master/imgs/ansel_adams3.jpg')
    result = color.inference(data='/home/user/下载/colorization-master/imgs/ansel_adams3.jpg',img_type='pil',show=True)
    color.show(result)
    color.format_output(lang="zh")
    color.save(result,"color_ou.jpg")


def kimi_stream_demo():
    import os
    from openai import OpenAI
    
    client = OpenAI(
        api_key="sk-c1nBfFK5mcwtilUBr6uvAVulwUhIBWNOqrbVZstvmwBXUcI9",
        base_url="https://api.moonshot.cn/v1",
    )
    
    response = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {
                "role": "system",
                "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。",
            },
            {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"},
        ],
        temperature=0.3,
        stream=True,
    )
    
    collected_messages = []
    for idx, chunk in enumerate(response):
        # print("Chunk received, value: ", chunk)
        chunk_message = chunk.choices[0].delta
        if not chunk_message.content:
            continue
        collected_messages.append(chunk_message)  # save the message
        print(f"#{idx}: {''.join([m.content for m in collected_messages])}")
    print(f"Full conversation received: {''.join([m.content for m in collected_messages])}")

def  llm_stream():
    import json
    import requests

    url = "https://api.moonshot.cn/v1"  # 替换为目标URL
    data = {
        "stream": True,
        "model": "moonshot-v1-8k",
        "messages": [
            {
                "role": "user",
                "content": "你是谁"
            },
        ]
    }
    headers = {
        "Authorization": "Bearer sk-c1nBfFK5mcwtilUBr6uvAVulwUhIBWNOqrbVZstvmwBXUcI9",
    }

    # 使用 with 语句确保请求完成后释放资源
    with requests.post(url, json=data, headers=headers, timeout=60000, stream=True) as response:
        # print(response.headers)
        for chunk in response.iter_lines(chunk_size=None):
            mChunk = chunk.decode('utf-8')
            if "[DONE]" in mChunk:
                break
            print(mChunk)
            lines = mChunk.splitlines()
            for line in lines:
                respStr = line.strip().replace("data: ", "")
                respContent = ""
                try:
                    respJson = json.loads(respStr)
                    respContent = respJson["choices"][0]["delta"]["content"]
                except  Exception as e:
                    respContent = ""
                print(respContent)

# 存储各种服务的API Key和URL
class ServiceProvider:
    BASE_URL = {
        "openrouter":"https://openrouter.ai/api/v1/chat/completions",
        "moonshot":"https://api.moonshot.cn/v1/chat/completions",
        "google": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBY-2VWbVvWybt8qjnruUY4tip4X_OwCp8"

    }
    API_KEY = {
        "openrouter": "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",
        "moonshot": "sk-c1nBfFK5mcwtilUBr6uvAVulwUhIBWNOqrbVZstvmwBXUcI9",
        "google": "AIzaSyBY-2VWbVvWybt8qjnruUY4tip4X_OwCp8"
    }
    MODEL = {
        "openrouter": "mistralai/mistral-7b-instruct:free",
        "moonshot": "moonshot-v1-8k",
        "google": "gemini-pro"
    }
    def __init__(self, service_name):
        self.api_key = ServiceProvider.API_KEY[service_name]
        self.url = ServiceProvider.BASE_URL[service_name]
        self.model = ServiceProvider.MODEL[service_name]
import requests
import json
class Client:
    """docstring for Client
    
    """

    def __init__(self, provider=None,base_url=None,api_key=None,model=None):
        self.provider = provider
        self.base_url = base_url
        self.api_key = api_key
        self.model = model

        if provider:
            self.api_key = ServiceProvider.API_KEY[provider]
            self.url = ServiceProvider.BASE_URL[provider]
            self.model = ServiceProvider.MODEL[provider]
    
    def inference(self, message, stream=False):
        if isinstance(message,str):
            messages = [{"role": "user", "content": message}]
        else:
            messages = message
        if stream:
            data = json.dumps({
                        "model": self.model, # Optional
                        "messages": messages,
                        "stream": stream,
                    })
        else:
            data = json.dumps({
                        "model": self.model, # Optional
                        "messages": messages,
                    })
        response = requests.post(
            url=self.url,
            headers={
                'Accept': 'text/event-stream',
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            data=data
            # stream=stream,
        )
        if stream:
            content = ''
            for output in response.iter_lines(chunk_size=None):
                # print("+++++++++++",output)
                if output==b'data: [DONE]':
                    break
                # 判断content是否为空
                elif output[:6] == b'data: ':
                    # print("------------",output[6:])
                    data = output[6:]
                    output = json.loads(data)
                    content = output["choices"][0]["delta"]["content"]# .encode('latin1').decode('utf-8')
        else:
            try:
                content = response.json()["choices"][0]["message"]
            except Exception as e:
                content = response.json()

        print(content)
        return content

def llm_demo(stream=False):
    from XEdu.LLM import Client
    print(Client.support_provider())
    # client = Client(provider="openrouter",api_key="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")
    client = Client(base_url="https://openrouter.ai/api/v1",api_key="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",model="mistralai/mistral-7b-instruct:free")
    # client = Client(provider="moonshot",api_key="sk-c1nBfFK5mcwtilUBr6uvAVulwUhIBWNOqrbVZstvmwBXUcI9")
    # client = Client(provider="deepseek",api_key="sk-bc3da8219e624f52a80b565a6aa31dcd")
    # client = Client(provider="glm",api_key="03a6c63bc0d356c5819f20b009b511e9.EMc2bCVDb7XJYuJf")
    # client = Client(provider="replicate",api_key="r8_HjFF0greljF48VQUFpCOUF021NSciu62QhRZP") # todo
    # print(client.support_model())
    # detail = client.model_info("deepseek-chat")
    # print(detail)
    res = client.inference("你好,用中文介绍一下你自己",stream=True)

def seg_demo():
    from XEdu.hub import Workflow as wf
    seg = wf(task='seg_sam') # iris act 
    img_p = '/home/user/下载/sam/efficientvit/assets/fig/cat.jpg'
    # img = 'ele.jpg'
    # img = 'fire.jpg'
    result, img = seg.inference(data=img_p,img_type='cv2',show=True,prompt=[[170,70],[380,270]])
    result, img = seg.inference(data=img_p,img_type='cv2',show=True,prompt=[[380,270]])
    seg.show(img)
    import time
    start = time.time()
    result,img = seg.inference(data=img_p,mode='box',prompt=[170,70,380,270],img_type='cv2',show=True)
    result,img = seg.inference(data=img_p,mode='box',prompt=[[170,70,380,270]],img_type='cv2',show=True)
    result,img = seg.inference(data=img_p,mode='box',prompt=[[170,70,380,270]],img_type='cv2',show=True)
    print(time.time()-start)
    # print(result.shape)
    seg.show(result[0])
    seg.show(img)
    seg.format_output(lang="zh")
    seg.save(img,"seg_ou.png")

if __name__ == "__main__":
    # pose_infer_demo()
    # det_infer_demo()
    # video_infer_demo()
    # hand_video_demo()
    # coco_det_demo()
    # hand_det_demo()
    # face_det_demo()
    # ocr_demo()
    # mmedu_demo()
    # custom_demo()
    # basenn_demo()
    # cls_demo()
    # baseml_demo()
    # style_demo()
    # qa_demo()
    # drive_demo()
    # embedding_demo()
    # color_demo()
    # llm_demo()
    # client = Client(provider="openrouter")
    # client.inference("你好,用中文介绍一下你自己")
    # llm_stream()
    seg_demo()


