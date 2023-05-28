
const prompt = require('prompt-sync')();
const shell = require('shelljs');

const config = require('./config.json');
const lang = require(`./lang/${config.language}.json`)


main();


function main() {
    console.log(lang.welcome)

    // take a screenshot for phone and do OCR
    screenshotOCRLoop()

    // check if we are at the last page

    // goto next page

}

// take a screenshot for phone and do OCR
function screenshotOCRLoop() {
    captureScreen()
}


// take screenshot for android, pull it to local, and delete it on android
// return the path of the screenshot
async function captureScreen(fileName = "screen.png") {
    console.log("@dev正在截图...")
    shell.exec(`adb shell screencap -p ${config.cache_location_android}/${fileName}`);
    shell.exec(`adb pull ${config.cache_location_android}/${fileName} ${config.cache_location_pc}/${fileName}`);
    shell.exec(`adb shell rm ${config.cache_location_android}/${fileName}`);
    console.log(`@dev截图完成, 图片已缓存到${config.cache_location_pc}/${fileName}`)
    return `${config.cache_location_pc}/${fileName}`
}










