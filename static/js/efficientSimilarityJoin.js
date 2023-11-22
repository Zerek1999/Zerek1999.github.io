
function downloadFile() {
    // 创建一个虚拟的下载链接
    var link = document.createElement('a');
    link.href = 'static/resources/efficientSimilarityJoin.py'; // 文件的路径
    link.download = 'efficientSimilarityJoin.py'; // 下载后保存的文件名

    // 将链接添加到页面
    document.body.appendChild(link);

    // 模拟点击链接触发下载
    link.click();

    // 从页面移除链接
    document.body.removeChild(link);
}


document.addEventListener('DOMContentLoaded', function() {
    var downloadButton = document.getElementById('download-button');
    downloadButton.addEventListener('click', downloadFile);
});