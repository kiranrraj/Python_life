import concurrent.futures
import requests
import time

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start = time.perf_counter()

def downloadImage(imgUrl):
    img_bytes = requests.get(imgUrl).content
    img_name = f"{'img-' + (imgUrl.split('/')[3]).split('-')[2]}.jpg"
    # print(img_name)
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"Finished downloading : {img_name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(downloadImage, img_urls)

finish = time.perf_counter()

print(f'Finished in {round(finish - start,2)} second(s)')

#output
# Finished downloading : img-fd2c41f4a759.jpg
# Finished downloading : img-c5c88640f235.jpg
# Finished downloading : img-fed454f93097.jpg
# Finished downloading : img-033611b8cc03.jpg
# Finished downloading : img-7ff8c1789d79.jpg
# Finished downloading : img-6633a470097c.jpg
# Finished downloading : img-452d3431c267.jpg
# Finished downloading : img-20a7a5813719.jpg
# Finished downloading : img-5ce911bafcde.jpg
# Finished downloading : img-a5f1f91d3b99.jpg
# Finished downloading : img-023c97d3f4b6.jpg
# Finished downloading : img-80185027ca84.jpg
# Finished downloading : img-acc6669e2f0c.jpg
# Finished downloading : img-609e1531270e.jpg
# Finished downloading : img-85c8e12f0c0e.jpg
# Finished in 70.86 second(s)