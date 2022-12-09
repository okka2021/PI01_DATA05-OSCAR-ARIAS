from fastapi import FastAPI, Path, UploadFile, File
from typing import Optional
from pydantic import BaseModel
import shutil

app=FastAPI()

@app.get("/year,plataform,duration")
def get_max_duration(year,plataform,duration):
    filter_df = final_df[final_df["plataform"] == plataform]
    filter_df = filter_df[filter_df["release_year"] == year]
    filter_df = filter_df.drop_duplicates(subset='title', keep="last")
    filter_df['duration_min'] = filter_df['duration'].str.split(' ').str[0].astype(float)
    final = filter_df.loc[filter_df['duration_min'] == max(filter_df["duration_min"])]
    final = final["title"].values[0]
    return final