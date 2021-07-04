const known_arr = [
  'repeat',
  '1YqKovX',
  'NDBCMjBnMzBpNTFKNjA2MDFcMzB3NDAxMzBBNDFqNDBcNDExMzBnNzB1MzBpMTBrMzBsNDA3NjB4NTBpNTBYMTBLMTBJNDBoNTBYMDBLNDFpNTFsNzA2NzBmNDBvMTA2NTA1NzBLMTFuNTE4NzA3NDFCNTAtMTE4NDB3MzFhMTByNDF6NzBLMzA9MjA9MTA9',
  'substr',
  'output',
  'getElementsByTagName',
  '65022JgPEZp',
  'keydown',
  'length',
  'innerHTML',
  '677PRUQAU',
  'ArrowLeft',
  'QWxTM3tCYXNFNjRfaTUrYjByTkluZ35cUXdvLy14SDhXekNqN3ZGRDJleVZrdHFPTDFHaEtZdWZtWmRKcFg5fQ==',
  '133781JKLWBV',
  'ArrowUp',
  '90407czXCgh',
  'PGRpdiBzdHlsZT0id2lkdGg6IDM1MHB4OyBwb3NpdGlvbjogYWJzb2x1dGU7IGJvdHRvbTogMHB4OyBsZWZ0OiAwcHg7Ij48ZGl2IHN0eWxlPSJ0ZXh0LWFsaWduOiBjZW50ZXI7IGFuaW1hdGlvbjogcmFpbmJvdyAycyBsaW5lYXIgMHMgaW5maW5pdGUgbm9ybWFsOyBwb3NpdGlvbjogYWJzb2x1dGU7IHRvcDogLTEwcHg7IGxlZnQ6IDUwJTsgZm9udC1zaXplOiAyMHB4OyB0cmFuc2Zvcm06IHRyYW5zbGF0ZVgoLTUwJSk7IHdpZHRoOiAzNTBweDsiPkhlcmUgaXMgeW91cjxicj4iZW5jb2RlZCIgZmxhZyw8YnI+aW5wdXQgdG8gZW5jb2RlIHNvbWV0aGluZyBlbHNlITwvZGl2PiA8c3ZnIGlkPSLwn5CIIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGlkPSJib2R5Ij48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJmaWxsIiBkdXI9IjUwMG1zIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIga2V5VGltZXM9IjA7MC4xOzAuMjswLjM7MC40OzAuNTswLjY7MC43OzAuODswLjk7MSIgdmFsdWVzPSIgI2ZmOGQ4YjsgI2ZlZDY4OTsgIzg4ZmY4OTsgIzg3ZmZmZjsgIzhiYjVmZTsgI2Q3OGNmZjsgI2ZmOGNmZjsgI2ZmNjhmNzsgI2ZlNmNiNzsgI2ZmNjk2ODsgI2ZmOGQ4YiAiPjwvYW5pbWF0ZT48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJkIiBkdXI9IjUwMG1zIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIga2V5VGltZXM9IjA7MC4xOzAuMjswLjM7MC40OzAuNTswLjY7MC43OzAuODswLjk7MSIgdmFsdWVzPSIgTTY3LjEsMTA5LjVjLTkuNiwwLTIzLjYtOC44LTIzLjYtMjRjMC0xMi4xLDE3LjgtNDEsMzcuNS00MWMxNS42LDAsMjMuMywxMC42LDI1LjEsMjAuNSBjMS45LDEwLjcsMy45LDguMiwzLjksMTkuNWMwLDguMi0zLjgsMTctMy44LDIyLjNjMCwzLjksMS40LDcuNCwyLjksMTAuNWMxLjcsMy41LDIuNCw2LjYsMi40LDkuMkg5LjVjMC0xMy43LDEwLjgtMTQsMjEuMS0yMyBjNS42LTQuOSwxMS0xMi40LDE0LjUtMjY7IE01Ni4xLDEwNy41Yy05LjYsMC0yNC42LTEzLjgtMjQuNi0yOWMwLTE2LjIsMTMtNDIsMzMuNS00MmMxNy44LDAsMjIuMywxMS42LDI2LjEsMjIuNSBjMy42LDEwLjMsOS45LDkuMiw5LjksMjAuNWMwLDguMi0xLjgsNy0xLjgsMTIuM2MwLDQuNSwzLjQsOC4yLDYuNCwxNC4xYzIuNSw0LjgsNC44LDExLjIsNC44LDIwLjZoLTk5YzAtMTIuMSw3LjItMTcuNiwxNC43LTI0LjMgYzMuMi0yLjksNi41LTUuOSw5LjItOS44OyBNNDUuMSwxMDkuNWMtNS41LTAuMi0yNy42LTguNC0yNy42LTI3YzAtMTcuOSwxNC44LTQyLDMyLjUtNDJjMTUuNCwwLDI0LDEwLjQsMjYuMSwyMS41IGMxLjMsNi43LDkuOSw5LjgsOS45LDIxLjVjMCw4LjItMC44LDYtMC44LDExLjNjMCw3LjcsMTIuOCw5LDIwLjgsMTVjNy43LDUuOCwxNS41LDE2LjcsMTUuNSwxNi43aC0xMTBjMC00LjgsMS43LTExLjMsNS0xNiBjMy4yLTQuNSw0LjUtOC4zLDUtMTU7IE0zNiwxMjBjLTUuNS0wLjItMjguNS0xMS45LTI4LjUtMzAuNWMwLTE2LjIsMTIuNS00MiwzMy00MmMxNy44LDAsMjEuOCw5LjYsMjUuNiwyMC41IEM2OS43LDc4LjMsNzYsNzguMiw3Niw4OS41YzAsOC4yLTAuOCw0LTAuOCw5LjNjMCw1LjksMTYuNSw3LjgsMjguNCwxNS45YzgsNS41LDE3LjksMTEuOCwxNy45LDExLjhoLTExMGMwLTIuMS0xLjItNS4yLTEuOS0xNC41IGMtMC4zLTMuNi0wLjUtOC4xLTAuNS0xMy45OyBNMzcsMTE5LjVjLTE1LDAuMS0zMy41LTEyLjctMzMuNS0zMEMzLjUsNzMuMywxNiw0NywzNi41LDQ3YzE3LjgsMCwyMi44LDExLDI2LDIyIEM2NS42LDc5LjQsNzMsNzkuMiw3Myw5MC41YzAsNC0xLjgsNi42LTEuOCw4LjNjMCw1LjksMTQuMiw2LjQsMjYuNCwxNS45YzcuNyw2LDEzLjksMTEuOCwxMy45LDExLjhINy41Yy0xLjItMy40LTEuOC03LjMtMS45LTExLjIgYy0wLjItNS4xLDAuMy0xMC4xLDAuOS0xMy43OyBNNDAuNSwxMjEuNWMtMTIuNiwwLTMwLTEzLjQtMzAtMjlDMTAuNSw3Ni4zLDIzLDUzLDQzLjUsNTNjMTQuNSwwLDIyLjgsOS42LDI1LDIyIGMxLjIsNi45LDEwLDkuMiwxMCwyMC41YzAsNCwwLDUuNiwwLDcuM2MwLDQuOSw2LjEsNy41LDExLjIsMTEuOWM1LjgsNSw3LjIsMTEuOCw3LjIsMTEuOEg4LjVjMC0xLjUtMC42LTYuMSwwLjQtMTEuOCBjMC42LTMuNSwxLjktNy41LDQuMy0xMS42OyBNNDguNSwxMjEuNWMtMTIuNiwwLTI1LTYuMy0yNS0xOGMwLTE2LjIsMTMuNy00NywzNi00N2MxNS42LDAsMjQuOCw5LjEsMjcsMjEuNSBjMS4yLDYuOSw3LDkuMiw3LDE4LjVjMCw5LjUtNCwxMS00LDIyYzAsNC4xLDAuNSw1LDEsNmMwLjUsMS4yLDEsMiwxLDJoLTgxYzAtNS4zLDMuMS04LjMsNi4zLTExLjVjMi42LTIuNiw1LjQtNS4zLDYuNy05LjU7IE02OC41LDEyMS41Yy0xMi42LDAtMzMtNS44LTMzLTIzYzAtOS4yLDExLjgtMzYsMzctMzZjMTUuNiwwLDI1LjgsOC4xLDI4LDIwLjUgYzEuMiw2LjksNCw2LjIsNCwxNS41YzAsOS41LTUsMTUuMS01LDIxYzAsMS45LDEsMi4zLDEsNWMwLDEuMiwwLDIsMCwyaC05MWMwLjUtNy42LDcuMS0xMS4xLDEzLjctMTUuN2M0LjktMy40LDkuOS03LjUsMTIuMy0xNC4zOyBNNzMuNSwxMTcuNWMtMTIuNiwwLTMwLTYuMi0zMC0yNWMwLTE0LjIsMjAuOS0zNywzOC0zN2MxNy42LDAsMjUuOCwxMS4xLDI4LDIzLjUgYzEuMiw2LjksMyw3LjIsMywxNi41YzAsMTIuMS02LDE2LjEtNiwyMmMwLDQuMiwyLDUuMywyLDhjMCwxLjIsMCwxLDAsMUg3LjVjMi4xLTkuNCwxMC40LTEzLjMsMTkuMi0xOS40IGM3LjEtNSwxNC40LTExLjUsMTguOC0yMy42OyBNODAuNSwxMTUuNWMtMTIuNiwwLTMyLTkuMi0zMi0yOGMwLTE0LjIsMjIuOS0zNSw0MC0zNWMxNy42LDAsMjUuOCwxMi4xLDI4LDI0LjUgYzEuMiw2LjksMyw2LjIsMywxNS41YzAsMTIuMS02LDE5LjEtNiwyNWMwLDQuMiwyLDUuMywyLDhjMCwxLjIsMCwxLDAsMWgtMTAyYzIuMy04LjcsMTEuNi0xMS43LDIwLjgtMjAuMSBjNS4zLTQuOCwxMC41LTExLjQsMTQuMi0yMS45OyBNNjcuMSwxMDkuNWMtOS42LDAtMjMuNi04LjgtMjMuNi0yNGMwLTEyLjEsMTcuOC00MSwzNy41LTQxYzE1LjYsMCwyMy4zLDEwLjYsMjUuMSwyMC41IGMxLjksMTAuNywzLjksOC4yLDMuOSwxOS41YzAsOC4yLTMuOCwxNy0zLjgsMjIuM2MwLDMuOSwxLjQsNy40LDIuOSwxMC41YzEuNywzLjUsMi40LDYuNiwyLjQsOS4ySDkuNWMwLTEzLjcsMTAuOC0xNCwyMS4xLTIzIGM1LjYtNC45LDExLTEyLjQsMTQuNS0yNiAiPjwvYW5pbWF0ZT48L3BhdGg+PHBhdGggaWQ9ImJlYWsiIGZpbGw9IiM3YjhjNjgiPjxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9ImQiIGR1cj0iNTAwbXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBrZXlUaW1lcz0iMDswLjE7MC4yOzAuMzswLjQ7MC41OzAuNjswLjc7MC44OzAuOTsxIiB2YWx1ZXM9IiBNNzguMjksNzBjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzc4LjI5LDg1LjUsNzguMjksNzBaOyBNNjIuMjksNjRjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzYyLjI5LDc5LjUsNjIuMjksNjRaOyBNNDguMjksNjdjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzQ4LjI5LDgyLjUsNDguMjksNjdaOyBNMzYuMjksNzNjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzM2LjI5LDg4LjUsMzYuMjksNzNaOyBNMzUuMjksNzVjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzM1LjI5LDkwLjUsMzUuMjksNzVaOyBNNDEuMjksODFjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzQxLjI5LDk2LjUsNDEuMjksODFaOyBNNTkuMjksODRjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzU5LjI5LDk5LjUsNTkuMjksODRaOyBNNzIuMjksODljMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzcyLjI5LDEwNC41LDcyLjI5LDg5WjsgTTgwLjI5LDgyYzAtOS45MiwyLjUtMTQsOC0xNHM4LDIuMTcsOCwxMC42N2MwLDE1LjkyLTcsMjYuMzMtNywyNi4zM1M4MC4yOSw5Ny41LDgwLjI5LDgyWjsgTTg3LjI5LDc4YzAtOS45MiwyLjUtMTQsOC0xNHM4LDIuMTcsOCwxMC42N2MwLDE1LjkyLTcsMjYuMzMtNywyNi4zM1M4Ny4yOSw5My41LDg3LjI5LDc4WjsgTTc4LjI5LDcwYzAtOS45MiwyLjUtMTQsOC0xNHM4LDIuMTcsOCwxMC42N2MwLDE1LjkyLTcsMjYuMzMtNywyNi4zM1M3OC4yOSw4NS41LDc4LjI5LDcwWiAiPjwvYW5pbWF0ZT48L3BhdGg+PGVsbGlwc2UgaWQ9ImV5ZS1yaWdodCIgcng9IjMiIHJ5PSI0Ij48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJjeCIgZHVyPSI1MDBtcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGtleVRpbWVzPSIwOzAuMTswLjI7MC4zOzAuNDswLjU7MC42OzAuNzswLjg7MC45OzEiIHZhbHVlcz0iMTAwOzg0OzcwOzU4OzU3OzYzOzgxOzk0OzEwMjsxMDk7MTAwIj48L2FuaW1hdGU+PGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iY3kiIGR1cj0iNTAwbXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBrZXlUaW1lcz0iMDswLjE7MC4yOzAuMzswLjQ7MC41OzAuNjswLjc7MC44OzAuOTsxIiB2YWx1ZXM9IjYyOzU2OzU5OzY1OzY3OzczOzc2OzgxOzc0OzcwOzYyIj48L2FuaW1hdGU+PC9lbGxpcHNlPjxlbGxpcHNlIGlkPSJleWUtbGVmdCIgcng9IjMiIHJ5PSI0Ij48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJjeCIgZHVyPSI1MDBtcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGtleVRpbWVzPSIwOzAuMTswLjI7MC4zOzAuNDswLjU7MC42OzAuNzswLjg7MC45OzEiIHZhbHVlcz0iNjcuNTs1MS41OzM3LjU7MjUuNTsyNC41OzMwLjU7NDguNTs2MS41OzY5LjU7NzYuNTs2Ny41Ij48L2FuaW1hdGU+PGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iY3kiIGR1cj0iNTAwbXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBrZXlUaW1lcz0iMDswLjE7MC4yOzAuMzswLjQ7MC41OzAuNjswLjc7MC44OzAuOTsxIiB2YWx1ZXM9IjYyOzU2OzU5OzY1OzY3OzczOzc2OzgxOzc0OzcwOzYyIj48L2FuaW1hdGU+PC9lbGxpcHNlPjwvc3ZnPjwvZGl2Pg==',
  '131837PcDnWL',
  '19pQimXL',
  '623605MIswVM',
  'charCodeAt',
  'join',
  '4WsUYDr',
  '686oWrfyq',
  'body',
  'map',
  'getElementById',
  'textContent',
  'match',
  'key',
  '302349wKdZHP',
  '4OYJFlQ',
  'input',
  'padStart',
  'Backspace',
];
function getDataFromArray(arg1, arg2) {
  arg1 = arg1 - 0x1c6;
  let ret = known_arr[arg1];
  return ret;
}
// shifting known_arr
(function (arg1, arg2) {
  const getDataFromArray_ = getDataFromArray;
  while (!![]) {
    try {
      const cal =   
        -parseInt('302349wKdZHP') +
        parseInt('65022JgPEZp') * -parseInt('4WsUYDr') +
        -parseInt('623605MIswVM') +
        -parseInt('4OYJFlQ') * parseInt('90407czXCgh') +
        -parseInt('133781JKLWBV') * parseInt('1YqKovX') +
        parseInt('686oWrfyq') * -parseInt('677PRUQAU') +
        parseInt('131837PcDnWL') * parseInt('19pQimXL');
      if (cal === arg2) break;    
      else arg1['push'](arg1['shift']());
    } catch (error) {
      arg1['push'](arg1['shift']());
    }
  }
})(known_arr, 0x57a76),

  (() => {
    const getDataFromArray = getDataFromArray,
      enc_new_info = 'PGRpdiBzdHlsZT0id2lkdGg6IDM1MHB4OyBwb3NpdGlvbjogYWJzb2x1dGU7IGJvdHRvbTogMHB4OyBsZWZ0OiAwcHg7Ij48ZGl2IHN0eWxlPSJ0ZXh0LWFsaWduOiBjZW50ZXI7IGFuaW1hdGlvbjogcmFpbmJvdyAycyBsaW5lYXIgMHMgaW5maW5pdGUgbm9ybWFsOyBwb3NpdGlvbjogYWJzb2x1dGU7IHRvcDogLTEwcHg7IGxlZnQ6IDUwJTsgZm9udC1zaXplOiAyMHB4OyB0cmFuc2Zvcm06IHRyYW5zbGF0ZVgoLTUwJSk7IHdpZHRoOiAzNTBweDsiPkhlcmUgaXMgeW91cjxicj4iZW5jb2RlZCIgZmxhZyw8YnI+aW5wdXQgdG8gZW5jb2RlIHNvbWV0aGluZyBlbHNlITwvZGl2PiA8c3ZnIGlkPSLwn5CIIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDEyOCAxMjgiIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIzIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGlkPSJib2R5Ij48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJmaWxsIiBkdXI9IjUwMG1zIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIga2V5VGltZXM9IjA7MC4xOzAuMjswLjM7MC40OzAuNTswLjY7MC43OzAuODswLjk7MSIgdmFsdWVzPSIgI2ZmOGQ4YjsgI2ZlZDY4OTsgIzg4ZmY4OTsgIzg3ZmZmZjsgIzhiYjVmZTsgI2Q3OGNmZjsgI2ZmOGNmZjsgI2ZmNjhmNzsgI2ZlNmNiNzsgI2ZmNjk2ODsgI2ZmOGQ4YiAiPjwvYW5pbWF0ZT48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJkIiBkdXI9IjUwMG1zIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSIga2V5VGltZXM9IjA7MC4xOzAuMjswLjM7MC40OzAuNTswLjY7MC43OzAuODswLjk7MSIgdmFsdWVzPSIgTTY3LjEsMTA5LjVjLTkuNiwwLTIzLjYtOC44LTIzLjYtMjRjMC0xMi4xLDE3LjgtNDEsMzcuNS00MWMxNS42LDAsMjMuMywxMC42LDI1LjEsMjAuNSBjMS45LDEwLjcsMy45LDguMiwzLjksMTkuNWMwLDguMi0zLjgsMTctMy44LDIyLjNjMCwzLjksMS40LDcuNCwyLjksMTAuNWMxLjcsMy41LDIuNCw2LjYsMi40LDkuMkg5LjVjMC0xMy43LDEwLjgtMTQsMjEuMS0yMyBjNS42LTQuOSwxMS0xMi40LDE0LjUtMjY7IE01Ni4xLDEwNy41Yy05LjYsMC0yNC42LTEzLjgtMjQuNi0yOWMwLTE2LjIsMTMtNDIsMzMuNS00MmMxNy44LDAsMjIuMywxMS42LDI2LjEsMjIuNSBjMy42LDEwLjMsOS45LDkuMiw5LjksMjAuNWMwLDguMi0xLjgsNy0xLjgsMTIuM2MwLDQuNSwzLjQsOC4yLDYuNCwxNC4xYzIuNSw0LjgsNC44LDExLjIsNC44LDIwLjZoLTk5YzAtMTIuMSw3LjItMTcuNiwxNC43LTI0LjMgYzMuMi0yLjksNi41LTUuOSw5LjItOS44OyBNNDUuMSwxMDkuNWMtNS41LTAuMi0yNy42LTguNC0yNy42LTI3YzAtMTcuOSwxNC44LTQyLDMyLjUtNDJjMTUuNCwwLDI0LDEwLjQsMjYuMSwyMS41IGMxLjMsNi43LDkuOSw5LjgsOS45LDIxLjVjMCw4LjItMC44LDYtMC44LDExLjNjMCw3LjcsMTIuOCw5LDIwLjgsMTVjNy43LDUuOCwxNS41LDE2LjcsMTUuNSwxNi43aC0xMTBjMC00LjgsMS43LTExLjMsNS0xNiBjMy4yLTQuNSw0LjUtOC4zLDUtMTU7IE0zNiwxMjBjLTUuNS0wLjItMjguNS0xMS45LTI4LjUtMzAuNWMwLTE2LjIsMTIuNS00MiwzMy00MmMxNy44LDAsMjEuOCw5LjYsMjUuNiwyMC41IEM2OS43LDc4LjMsNzYsNzguMiw3Niw4OS41YzAsOC4yLTAuOCw0LTAuOCw5LjNjMCw1LjksMTYuNSw3LjgsMjguNCwxNS45YzgsNS41LDE3LjksMTEuOCwxNy45LDExLjhoLTExMGMwLTIuMS0xLjItNS4yLTEuOS0xNC41IGMtMC4zLTMuNi0wLjUtOC4xLTAuNS0xMy45OyBNMzcsMTE5LjVjLTE1LDAuMS0zMy41LTEyLjctMzMuNS0zMEMzLjUsNzMuMywxNiw0NywzNi41LDQ3YzE3LjgsMCwyMi44LDExLDI2LDIyIEM2NS42LDc5LjQsNzMsNzkuMiw3Myw5MC41YzAsNC0xLjgsNi42LTEuOCw4LjNjMCw1LjksMTQuMiw2LjQsMjYuNCwxNS45YzcuNyw2LDEzLjksMTEuOCwxMy45LDExLjhINy41Yy0xLjItMy40LTEuOC03LjMtMS45LTExLjIgYy0wLjItNS4xLDAuMy0xMC4xLDAuOS0xMy43OyBNNDAuNSwxMjEuNWMtMTIuNiwwLTMwLTEzLjQtMzAtMjlDMTAuNSw3Ni4zLDIzLDUzLDQzLjUsNTNjMTQuNSwwLDIyLjgsOS42LDI1LDIyIGMxLjIsNi45LDEwLDkuMiwxMCwyMC41YzAsNCwwLDUuNiwwLDcuM2MwLDQuOSw2LjEsNy41LDExLjIsMTEuOWM1LjgsNSw3LjIsMTEuOCw3LjIsMTEuOEg4LjVjMC0xLjUtMC42LTYuMSwwLjQtMTEuOCBjMC42LTMuNSwxLjktNy41LDQuMy0xMS42OyBNNDguNSwxMjEuNWMtMTIuNiwwLTI1LTYuMy0yNS0xOGMwLTE2LjIsMTMuNy00NywzNi00N2MxNS42LDAsMjQuOCw5LjEsMjcsMjEuNSBjMS4yLDYuOSw3LDkuMiw3LDE4LjVjMCw5LjUtNCwxMS00LDIyYzAsNC4xLDAuNSw1LDEsNmMwLjUsMS4yLDEsMiwxLDJoLTgxYzAtNS4zLDMuMS04LjMsNi4zLTExLjVjMi42LTIuNiw1LjQtNS4zLDYuNy05LjU7IE02OC41LDEyMS41Yy0xMi42LDAtMzMtNS44LTMzLTIzYzAtOS4yLDExLjgtMzYsMzctMzZjMTUuNiwwLDI1LjgsOC4xLDI4LDIwLjUgYzEuMiw2LjksNCw2LjIsNCwxNS41YzAsOS41LTUsMTUuMS01LDIxYzAsMS45LDEsMi4zLDEsNWMwLDEuMiwwLDIsMCwyaC05MWMwLjUtNy42LDcuMS0xMS4xLDEzLjctMTUuN2M0LjktMy40LDkuOS03LjUsMTIuMy0xNC4zOyBNNzMuNSwxMTcuNWMtMTIuNiwwLTMwLTYuMi0zMC0yNWMwLTE0LjIsMjAuOS0zNywzOC0zN2MxNy42LDAsMjUuOCwxMS4xLDI4LDIzLjUgYzEuMiw2LjksMyw3LjIsMywxNi41YzAsMTIuMS02LDE2LjEtNiwyMmMwLDQuMiwyLDUuMywyLDhjMCwxLjIsMCwxLDAsMUg3LjVjMi4xLTkuNCwxMC40LTEzLjMsMTkuMi0xOS40IGM3LjEtNSwxNC40LTExLjUsMTguOC0yMy42OyBNODAuNSwxMTUuNWMtMTIuNiwwLTMyLTkuMi0zMi0yOGMwLTE0LjIsMjIuOS0zNSw0MC0zNWMxNy42LDAsMjUuOCwxMi4xLDI4LDI0LjUgYzEuMiw2LjksMyw2LjIsMywxNS41YzAsMTIuMS02LDE5LjEtNiwyNWMwLDQuMiwyLDUuMywyLDhjMCwxLjIsMCwxLDAsMWgtMTAyYzIuMy04LjcsMTEuNi0xMS43LDIwLjgtMjAuMSBjNS4zLTQuOCwxMC41LTExLjQsMTQuMi0yMS45OyBNNjcuMSwxMDkuNWMtOS42LDAtMjMuNi04LjgtMjMuNi0yNGMwLTEyLjEsMTcuOC00MSwzNy41LTQxYzE1LjYsMCwyMy4zLDEwLjYsMjUuMSwyMC41IGMxLjksMTAuNywzLjksOC4yLDMuOSwxOS41YzAsOC4yLTMuOCwxNy0zLjgsMjIuM2MwLDMuOSwxLjQsNy40LDIuOSwxMC41YzEuNywzLjUsMi40LDYuNiwyLjQsOS4ySDkuNWMwLTEzLjcsMTAuOC0xNCwyMS4xLTIzIGM1LjYtNC45LDExLTEyLjQsMTQuNS0yNiAiPjwvYW5pbWF0ZT48L3BhdGg+PHBhdGggaWQ9ImJlYWsiIGZpbGw9IiM3YjhjNjgiPjxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9ImQiIGR1cj0iNTAwbXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBrZXlUaW1lcz0iMDswLjE7MC4yOzAuMzswLjQ7MC41OzAuNjswLjc7MC44OzAuOTsxIiB2YWx1ZXM9IiBNNzguMjksNzBjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzc4LjI5LDg1LjUsNzguMjksNzBaOyBNNjIuMjksNjRjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzYyLjI5LDc5LjUsNjIuMjksNjRaOyBNNDguMjksNjdjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzQ4LjI5LDgyLjUsNDguMjksNjdaOyBNMzYuMjksNzNjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzM2LjI5LDg4LjUsMzYuMjksNzNaOyBNMzUuMjksNzVjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzM1LjI5LDkwLjUsMzUuMjksNzVaOyBNNDEuMjksODFjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzQxLjI5LDk2LjUsNDEuMjksODFaOyBNNTkuMjksODRjMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzU5LjI5LDk5LjUsNTkuMjksODRaOyBNNzIuMjksODljMC05LjkyLDIuNS0xNCw4LTE0czgsMi4xNyw4LDEwLjY3YzAsMTUuOTItNywyNi4zMy03LDI2LjMzUzcyLjI5LDEwNC41LDcyLjI5LDg5WjsgTTgwLjI5LDgyYzAtOS45MiwyLjUtMTQsOC0xNHM4LDIuMTcsOCwxMC42N2MwLDE1LjkyLTcsMjYuMzMtNywyNi4zM1M4MC4yOSw5Ny41LDgwLjI5LDgyWjsgTTg3LjI5LDc4YzAtOS45MiwyLjUtMTQsOC0xNHM4LDIuMTcsOCwxMC42N2MwLDE1LjkyLTcsMjYuMzMtNywyNi4zM1M4Ny4yOSw5My41LDg3LjI5LDc4WjsgTTc4LjI5LDcwYzAtOS45MiwyLjUtMTQsOC0xNHM4LDIuMTcsOCwxMC42N2MwLDE1LjkyLTcsMjYuMzMtNywyNi4zM1M3OC4yOSw4NS41LDc4LjI5LDcwWiAiPjwvYW5pbWF0ZT48L3BhdGg+PGVsbGlwc2UgaWQ9ImV5ZS1yaWdodCIgcng9IjMiIHJ5PSI0Ij48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJjeCIgZHVyPSI1MDBtcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGtleVRpbWVzPSIwOzAuMTswLjI7MC4zOzAuNDswLjU7MC42OzAuNzswLjg7MC45OzEiIHZhbHVlcz0iMTAwOzg0OzcwOzU4OzU3OzYzOzgxOzk0OzEwMjsxMDk7MTAwIj48L2FuaW1hdGU+PGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iY3kiIGR1cj0iNTAwbXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBrZXlUaW1lcz0iMDswLjE7MC4yOzAuMzswLjQ7MC41OzAuNjswLjc7MC44OzAuOTsxIiB2YWx1ZXM9IjYyOzU2OzU5OzY1OzY3OzczOzc2OzgxOzc0OzcwOzYyIj48L2FuaW1hdGU+PC9lbGxpcHNlPjxlbGxpcHNlIGlkPSJleWUtbGVmdCIgcng9IjMiIHJ5PSI0Ij48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJjeCIgZHVyPSI1MDBtcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiIGtleVRpbWVzPSIwOzAuMTswLjI7MC4zOzAuNDswLjU7MC42OzAuNzswLjg7MC45OzEiIHZhbHVlcz0iNjcuNTs1MS41OzM3LjU7MjUuNTsyNC41OzMwLjU7NDguNTs2MS41OzY5LjU7NzYuNTs2Ny41Ij48L2FuaW1hdGU+PGFuaW1hdGUgYXR0cmlidXRlTmFtZT0iY3kiIGR1cj0iNTAwbXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBrZXlUaW1lcz0iMDswLjE7MC4yOzAuMzswLjQ7MC41OzAuNjswLjc7MC44OzAuOTsxIiB2YWx1ZXM9IjYyOzU2OzU5OzY1OzY3OzczOzc2OzgxOzc0OzcwOzYyIj48L2FuaW1hdGU+PC9lbGxpcHNlPjwvc3ZnPjwvZGl2Pg==',
      enc_2 = 'NDBCMjBnMzBpNTFKNjA2MDFcMzB3NDAxMzBBNDFqNDBcNDExMzBnNzB1MzBpMTBrMzBsNDA3NjB4NTBpNTBYMTBLMTBJNDBoNTBYMDBLNDFpNTFsNzA2NzBmNDBvMTA2NTA1NzBLMTFuNTE4NzA3NDFCNTAtMTE4NDB3MzFhMTByNDF6NzBLMzA9MjA9MTA9',
      enc_3 = 'QWxTM3tCYXNFNjRfaTUrYjByTkluZ35cUXdvLy14SDhXekNqN3ZGRDJleVZrdHFPTDFHaEtZdWZtWmRKcFg5fQ==',
      _0x2a3765 = 0x8,
      const1 = 0xa;
    let el_input,
      cond1 = 0x0;
    function func1(arg) {
      const getDataFromArray = getDataFromArray;
      if (!arg['length']) return '';
      let input_str = '',
        displayStr = '',
        _0x5395cb = 0x0;
      // a string by concanting every char in left padding 8 digit binary form
      for (let i = 0x0; i < arg['length']; i++ )  
        input_str += arg['charCodeAt'](i)['toString'](0x2)['padStart'](0x8, '0');   // get char code  // get binary represent   // pad left 0s to 8 digit
      // padding 0 at right to 10*k length
      _0x5395cb = (input_str['length'] %  const1) / 0x2 - 0x1;
      if (_0x5395cb != -0x1)
        input_str += '0'['repeat'](
          const1 - (input_str['length'] % const1)
        );
      // list1 = input_str.split(10 digit)
      list1 = input_str['match'](/(.{1,10})/g);
      // Display encoded flag
      for (let item of list1) {
        let num = parseInt(item, 0x2);
        displayStr += displayChar(
          (num >> 0x6) & 0x7,
          num >> 0x9,
          atob(enc_3)[num & 0x3fj]
        );
      }
      // padding encoded flag length 
      for (; _0x5395cb > 0x0; _0x5395cb--) {
        displayStr += displayChar(_0x5395cb % _0x2a3765, 0x0, '=');
      }
      return displayStr;
    }
    let displayChar = (arg1, arg2, arg3) =>
        '<span><div\x20class=\x22c' +
        arg1 +
        '\x20r' +
        arg2 +
        '\x22>' +
        arg3 +
        '</div></span>',
      toFunc1 = (arg) =>
        (document['getElementById']('output')['innerHTML'] =
          func1(arg));

    document['addEventListener']('keydown', (event) => {
      const getDataFromArray_ = getDataFromArray;
      if (event['key'] === 'Backspace' && cond1 == 0xa)
        el_input['textContent'] = el_input['textContent'][
          'substr'
        ](0x0, el_input['textContent']['length'] - 0x1);
      else {
        if (event['key'] === 'ArrowUp' && !(cond1 >> 0x1))
          return (cond1 += 0x1);
        else {
          if (
            event['key'] === 'ArrowDown' &&
            !(cond1 >> 0x2)
          )
            return (cond1 += 0x1);
          else {
            if (
              event['key'] === 'ArrowLeft' &&
              (cond1 == 0x4 || cond1 == 0x6)
            )
              return (cond1 += 0x1);
            else {
              if (
                event['key'] === 'ArrowRight' &&
                (cond1 == 0x5 || cond1 == 0x7)
              )
                return (cond1 += 0x1);
              else {
                if (event['key'] === 'b' && cond1 == 0x8)
                  return (cond1 += 0x1);
                else {
                  if (event['key'] === 'a' && cond1 == 0x9)
                    return (
                      (document['getElementsByTagName']('body')[0x0][  // add new content to website
                        'innerHTML'
                      ] += atob(enc_new_info)),
                      (el_input = document['getElementById'](           // unlock input
                        'input'
                      )),
                      (el_input['innerHTML'] = ''),                     // unlock input
                      (document['getElementById']('output')['innerHTML'] =  // add encoded flag
                        atob(enc_2)
                          ['match'](/(.{1,3})/g)
                          ['map']((char) =>
                            displayChar(
                              char[0x0],
                              char[0x1],
                              char[0x2]
                            )
                          )
                          ['join']('')),
                      (cond1 += 0x1)
                    );
                  else {
                    if (
                      event['key']['length'] == 0x1 &&
                      cond1 == 0xa
                    )
                      el_input['textContent'] += String['fromCharCode'](
                        event['key']['charCodeAt']()
                      );
                    else return;
                  }
                }
              }
            }
          }
        }
      }
      toFunc1(el_input['textContent']);
    });
  })();
