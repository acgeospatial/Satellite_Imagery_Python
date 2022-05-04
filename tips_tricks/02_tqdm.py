from tqdm import tqdm
import time

# just wrap any iterable with tqdm(iterable)

# for i in tqdm (range(100)):
#     time.sleep(0.01)

for i in tqdm (range(100), desc="Loading..."):
    # perhaps don't do this in real life!
    for k in range(100):
        time.sleep(0.01)
    time.sleep(0.01)
