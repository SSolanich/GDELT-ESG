"""
con este programa se descargan las tablas de gdelt (gkg) de un archivo tipo masterfilelist.txt previamente filtrado
y se suben a s3.
"""

import pandas as pd
from multiprocessing import Pool
import numpy as np
from time import time

def download_csv(link_slice):
    import urllib.request as req
    import zipfile
    import os
    from io import BytesIO
    import boto3
    from time import time
    iteration = 0
    timeout = 350
    done = False
    while not done:
        start_time = time()
        my_id = os.getpid()
        s3 = boto3.client("s3")
        work_msg = f"process {my_id} working" if iteration==0 else f"process {my_id} working for the {iteration + 1} time"
        print(work_msg)
        done = True
        for url in link_slice:
            if time() - start_time > timeout:
                print(f"process {my_id} timed out, restarting")
                done = False
                iteration += 1
                break
            try:
                filedata = req.urlopen(url)
                zipdata = BytesIO()
                zipdata.write(filedata.read())
                zipf = zipfile.ZipFile(zipdata)
                csv_filename = url.split('/')[-1][:-4]
                inside_file = zipf.open(csv_filename)
                s3.upload_fileobj(inside_file, "esg-gdelt", f"gkg-data/english/{csv_filename}")
            except:
                pass
    print(f"process {my_id} finished in {int(time() - start_time)} seconds.")
    return 0

def download_to_s3(n, dframe):
    p = 16  # numero de particiones y procesos
    # se trabaja el listado de links en partes de tamaño 1000 donde a cada proceso se le entregan 1000/p = 62 links
    data_split = np.array_split(dframe["link"][(n-1) * 1000:n * 1000], p)
    pool = Pool(p)
    pool.map(download_csv, data_split)
    pool.close()
    print("pool closed")
    pool.join()
    print("join")

if __name__ == "__main__":
    df = pd.read_csv("english.gkg.oct2020-feb2021.txt")
    t0 = time()
    for n in range(104):
        download_to_s3(n, df)
        print(f"iteration {n} took:", int(time() - t0), "seconds")
        t0 = time()

