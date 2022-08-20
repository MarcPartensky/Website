var url = $("#code-form").attr("action");

var basePath = 'https://cdn.rawgit.com/Petlja/pygame4skulpt/3435847b/pygame/';
Sk.externalLibraries = {
    pygame: {
        path: basePath + '__init__.js',
    },
    'pygame.display': {
        path: basePath + 'display.js',
    },
    'pygame.draw': {
        path: basePath + 'draw.js',
    },
    'pygame.event': {
        path: basePath + 'event.js',
    },
    'pygame.font': {
        path: basePath + 'font.js',
    },
    'pygame.image': {
        path: basePath + 'image.js',
    },
    'pygame.key': {
        path: basePath + 'key.js',
    },
    'pygame.mouse': {
        path: basePath + 'mouse.js',
    },
    'pygame.time': {
        path: basePath + 'time.js',
    },
    'pygame.transform': {
        path: basePath + 'transform.js',
    },
    'pygame.version': {
        path: basePath + 'version.js',
    },
  numpy : {
    path: 'https://raw.githubusercontent.com/ebertmi/skulpt_numpy/master/dist/numpy/__init__.js',
    dependencies: ['https://raw.githubusercontent.com/ebertmi/skulpt_numpy/master/deps/math.js'],
  },
  'numpy.random' : {
    path: 'https://raw.githubusercontent.com/ebertmi/skulpt_numpy/master/dist/numpy/random/__init__.js',
    dependencies: ['https://raw.githubusercontent.com/ebertmi/skulpt_numpy/master/deps/math.js'],
  },
  matplotlib : {
    path: 'https://raw.githubusercontent.com/ebertmi/skulpt_matplotlib/master/matplotlib/__init__.js',
  },
  'matplotlib.pyplot' : {
    path: 'https://raw.githubusercontent.com/ebertmi/skulpt_matplotlib/master/matplotlib/pyplot/__init__.js',
    dependencies: [
      'https://raw.githubusercontent.com/ebertmi/skulpt_matplotlib/master/deps/d3.min.js',
      'https://raw.githubusercontent.com/ebertmi/skulpt_matplotlib/master/deps/jquery.js',
    ],
  },
  'turtle': {
    path: 'https://raw.githubusercontent.com/trinketapp/turtle/master/__init__.js',
  }
};

$(window).bind("resize", function(){
    var w = $(window).width();
    var h = $(window).height();

    $("#mycanvas").css("width", w + "px");
    $("#mycanvas").css("height", h + "px");
});

isFullscreen = false

function toggleFullscreen() {
    if (isFullscreen) {
        //now i want to cancel fullscreen
        document.webkitCancelFullScreen(); //Chrome
        document.mozCancelFullScreen(); //Firefox
    } else {
        //using HTML5 for fullscreen (only newest Chrome + FF)
        $("#mycanvas")[0].webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT); //Chrome
        $("#mycanvas")[0].mozRequestFullScreen(); //Firefox
    }

}

function saveTextAsFile() {
  var textToWrite = editor.getValue();
  var textFileAsBlob = new Blob([textToWrite], {
    type: "text/plain;charset=utf-8"
  });
    var filename = document.getElementById('filename')
  var fileNameToSaveAs = filename.value || filename.placeholder

  var downloadLink = document.createElement("a");
  downloadLink.download = fileNameToSaveAs;
  downloadLink.innerHTML = "Download File";
  if (window.webkitURL != null) {
    // Chrome allows the link to be clicked
    // without actually adding it to the DOM.
    downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
  } else {
    // Firefox requires the link to be added to the DOM
    // before it can be clicked.
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
  }

  downloadLink.click();
}

var input = document.getElementById("filename");
input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        saveTextAsFile()
    }
});

CodeMirror.commands.save = saveTextAsFile;
var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
	theme: "material-palenight",
	lineNumbers: true,
	mode: "text/x-python",
	keyMap: "vim",
	matchBrackets: true,
	showCursorWhenSelecting: true
});
var commandDisplay = document.getElementById('command-display');
var keys = '';
CodeMirror.on(editor, 'vim-keypress', function(key) {
	keys = keys + key;
	commandDisplay.innerText = keys;
});
CodeMirror.on(editor, 'vim-command-done', function(e) {
	keys = '';
	commandDisplay.innerHTML = keys;
});
var vimMode = document.getElementById('vim-mode');
CodeMirror.on(editor, 'vim-mode-change', function(e) {
	vimMode.innerText = JSON.stringify(e);
});


// output functions are configurable.  This one just appends some text
// to a pre element.
function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
}


function builtinRead(file) {
  console.log("Attempting file: " + Sk.ffi.remapToJs(file));

  if (Sk.builtinFiles === undefined || Sk.builtinFiles.files[file] === undefined) {
    throw "File not found: '" + file + "'";
  }

  return Sk.builtinFiles.files[file];
}

// Here's everything you need to run a python program in skulpt
// grab the code from your textarea
// get a reference to your pre element for output
// configure the output function
// call Sk.importMainWithBody()



// Sk.main_canvas = document.getElementById("mycanvas");

function runit() {
	var modalTitle = document.getElementById('modal-title')
	var filename = document.getElementById('filename')
	modalTitle.innerHTML = filename.value || filename.placeholder

 var prog = editor.getValue()
 var output = document.getElementById("output");
 output.innerHTML = '';
 Sk.pre = "output";
 Sk.configure({output:outf, read:builtinRead});
 (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';


 var myPromise = Sk.misceval.asyncToPromise(function() {
		 return Sk.importMainWithBody("<stdin>", false, prog, true);
 });
 myPromise.then(function(mod) {
		 console.log('success');
 },
 function(err) {
		 output.innerHTML = '<div class="alert alert-danger" role="alert">'+err.toString()+'</div>'
 });
}
console.log('loaded editor.js')
