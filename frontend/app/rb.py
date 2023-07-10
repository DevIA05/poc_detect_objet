from roboflow import Roboflow
rf = Roboflow(api_key="bSNWf1JxDayUnaEuKW32")
project = rf.workspace().project("mask-wearing")
model = project.version(18).model

# infer on a local image
# print(model.predict("mask.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("../ressource/image/mask.jpg", confidence=40, overlap=30).save("../ressource/image/prediction1.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())


