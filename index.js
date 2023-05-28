
const prompt = require('prompt-sync')();
const shell = require('shelljs');
const tesseract = require('node-tesseract-ocr');
const fs = require('fs');

const config = require('./config.json');
const lang = require(`./lang/${config.language}.json`)


main();


async function main() {
    console.log(lang.welcome)

    // take a screenshot for phone and do OCR
    await screenshotOCRLoop()

    // check if we are at the last page

    // goto next page

}

// take a screenshot for phone and do OCR
async function screenshotOCRLoop() {
    let imgPath = captureScreen();
    let text = await ocr(imgPath);
    writeFile(config.cache_location_pc, "ocr.txt", text, "@dev识别结果已写入ocr.txt", "@dev识别结果写入失败")
}


// take screenshot for android, pull it to local, and delete it on android
// return the path of the screenshot
function captureScreen(fileName = "screen.png") {
    console.log("@dev正在截图...")
    shell.exec(`adb shell screencap -p ${config.cache_location_android}/${fileName}`);
    shell.exec(`adb pull ${config.cache_location_android}/${fileName} ${config.cache_location_pc}/${fileName}`);
    shell.exec(`adb shell rm ${config.cache_location_android}/${fileName}`);
    console.log(`@dev截图完成, 图片已缓存到${config.cache_location_pc}/${fileName}`)
    return `${config.cache_location_pc}/${fileName}`
}

// do OCR on the image
// return the text
async function ocr(imgPath, tesseractConfig = config.tesseract_config) {

    console.log("@dev正在识别...")
    const text = await tesseract.recognize(imgPath, tesseractConfig)
    console.log("@dev识别完成")
    return text
}



// ! General Tools

// encapsulated fs.writeFile, if write failed, retry 10 times recursively
// dir: file path, fileName: file name, data: file content, 
// successMessage: success message, errMessage: error message, 
// attempts: retry counter. Don't change it when calling this function
function writeFile(dir, fileName, data, successMessage, errMessage, attempts = 1) {

    fs.writeFile(`${dir}/${fileName}`, data, function (err) {
        if (err) {
            console.log(errMessage)
            console.log(err);
            if (attempts >= 10) {
                console.log(`@dev #####! --- 寫入錯誤, 已重试10次, 請檢查系統 ######`)
                return false
            }
            else {
                console.log(`@dev #####! --- 寫入錯誤, 正在重试: ${attempts + 1}/10 ######`)
                return writeFile(dir, fileName, data, successMessage, errMessage, attempts + 1);
            }
        };
        console.log(successMessage);
        return true;
    });
}







