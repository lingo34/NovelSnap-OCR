

general_config = {
    "ui_language": "zh_cn",
    "text_output_location": "./output/",
    "cache_location_pc": "./cache",
    "cache_location_android": "/sdcard",
}

ocr_config = {
    "rec_root": "./ocr_models/",
    # for available models, see CnOCR documentation https://cnocr.readthedocs.io/zh/latest/models/#_3
    # "rec_model_name": "ch_PP-OCRv3"
    "rec_model_name": "densenet_lite_136-gru",
    "resized_shape": (3200, 1440),

    # ignore the top/bottom x pixels of the image when ocr
    "top_ignore": 182,
    "bottom_ignore": 84,
    "min_box_size": 35
}


