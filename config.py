

general_config = {
    "ui_language": "zh_cn",
    "cache_location_pc": "./cache",
    "cache_location_android": "/sdcard",
}

ocr_config = {
    "rec_root": "./ocr_models/",
    # for available models, see CnOCR documentation https://cnocr.readthedocs.io/zh/latest/models/#_3
    # "rec_model_name": "ch_PP-OCRv3"
    "rec_model_name": "densenet_lite_136-gru",

    "resized_shape": (3200, 1440)
}


