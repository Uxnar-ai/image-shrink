# pic — shrink an image in the browser

> Drop a large image, set a max edge and quality, and see the before/after size, dimensions and saving in real time — then download. Nothing is uploaded.

English | [中文](README.md)

## What it is

Email attachments and upload forms love to cap images at 2 MB. This page does the compression in the browser: redraw onto a canvas and re-encode with toBlob, so the file never leaves the machine.

The long edge is scaled proportionally and small images are never upscaled. Output can be JPG, WebP or PNG; PNG ignores the quality slider because it is lossless. Converting PNG to JPG paints a white background first, otherwise transparent areas turn black. Phone photos with EXIF orientation are read through the imageOrientation option of createImageBitmap so portrait shots do not come out sideways.

A 2400×1600 sample image is drawn on load (canvas gradient plus dots), so the page is usable before you find a photo. Measured on that sample: 281.5 KB down to 76.4 KB at a 1600 long edge and quality 80, a 73% saving.

## Features

- Drag or pick a file; JPG, PNG and WebP supported
- Max-edge and quality sliders with live results
- Side-by-side preview showing pixels, bytes and percentage saved
- Output JPG, WebP or PNG; PNG ignores quality
- EXIF orientation respected, portrait photos stay upright
- Ships with a generated sample image so it works immediately
- Everything local — the image is never uploaded

## Stack

Python 3.12 · Flask 3.1 · 原生 JS · Canvas

## Run

```bash
pip install -r requirements.txt
python app.py  # 默认 127.0.0.1:8884
```

## About

Part of the **auto-lab** series — small projects written, deployed and maintained automatically by [Nix](https://github.com/Uxnar-ai) on a self-hosted server.

Placeholders such as `<SERVER_IP>` and `<LOCAL_PATH>` are sanitised values applied at publish time. This repository contains no credentials, internal addresses or personal data.

## License

MIT
