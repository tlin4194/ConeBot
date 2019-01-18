function XHRpromise(method, url, opts = {}) {
    const {
        withCredentials = true,
        body,
        contentType,
        successStatus = null
    } = opts;

    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method, url);
        xhr.withCredentials = withCredentials;

        contentType && xhr.setRequestHeader('Content-Type', contentType);
        xhr.onreadystatechange = () => {
            if (xhr.readyState !== xhr.DONE) {
                return;
            }

            if (successStatus !== null && xhr.status !== successStatus) {
                return reject(new Error(
                    `'${method} ${url}' failed: `
                    + `expected status ${successStatus}, got ${xhr.status}`
                ));
            }

            return resolve(xhr);
        };

        xhr.send(body);
    });
}

const keybinds = {
    w: 'fwd',
    s: 'bck',
    a: 'ccw',
    d: 'cw',
    ArrowUp: 'armup',
    ArrowDown: 'armhover',
    Enter: 'armdown',
    Backspace: 'armrelease'
}

let cmdPending = null;
function queue(executor) {
    const prevCmd = cmdPending;
    cmdPending = (async function() {
        await prevCmd;

        try {
            await executor();
        } finally {
            cmdPending = null;
        }
    }());

    return cmdPending;
}

function reset() {
    return queue(async function() {
        await XHRpromise('GET', '/reset', { successStatus: 200 });
    });
}

function controlsInit(elem) {
    let keyDown = false;

    elem.onkeydown = async function onKeyDown(event) {
        if (keyDown) {
            return;
        }

        keyDown = true;

        const { key } = event;
        if (key === ' ') {
            await reset();
        }

        if (!(key in keybinds)) {
            return;
        }

        const cmd = keybinds[key];
        await queue(async function() {
            await XHRpromise('GET', `/teleop/${cmd}`, { success: 200 });
        });
    }

    elem.onkeyup = async function onKeyUp(event) {
        if (!keyDown) {
            return;
        }

        keyDown = false;
        await reset();
    }
}

window.onload = function() {
    controlsInit(document.body);
}

