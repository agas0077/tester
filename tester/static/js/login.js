'use strict';

(function () {

    var inputLogin = document.getElementById('id_username');
    var inputPassword = document.getElementById('id_password');

    var eyeFirstLeft = document.querySelector('.animation__eye--one-one');
    var eyeFirstRight = document.querySelector('.animation__eye--one-two');

    var eyeSecondLeft = document.querySelector('.animation__eye--two-one');
    var eyeSecondRight = document.querySelector('.animation__eye--two-two');

    inputLogin.addEventListener('focus', firstFocusHandler);
    inputPassword.addEventListener('focus', firstFocusHandler);

    inputLogin.addEventListener('input', inputHandler);
    inputPassword.addEventListener('input', inputHandler);

    inputLogin.addEventListener('blur', blurHandler);
    inputPassword.addEventListener('blur', blurHandler);

    function firstFocusHandler() {
        var animation = document.querySelector('.animation');
        var animationVideo = document.querySelector('.animation__video');
        var eye = document.querySelectorAll('.animation__eye');
        var button = document.querySelector('.btn');
        var about = document.querySelector('.about');

        for (var i = 0; i < eye.length; i++) {
            eye[i].style.display = 'block';
            fadeIn(eye[i], 2000);
        }

        animation.style.maxHeight = '374px';
        animationVideo.style.display = 'block';
        fadeIn(animationVideo, 2000);
        about.style.display = 'inline';
        fadeIn(about, 2000);
        animationVideo.play();

        inputLogin.removeEventListener('focus', firstFocusHandler);
        inputPassword.removeEventListener('focus', firstFocusHandler);

        inputLogin.addEventListener('focus', focusHandler);
        inputPassword.addEventListener('focus', focusHandler);

        button.addEventListener('click', clickHandler);
    }

    function fadeIn(elem, speed) {
        var inInterval = setInterval(function () {
            elem.style.opacity = Number(elem.style.opacity) + 0.02;
            if (elem.style.opacity >= 1)
                clearInterval(inInterval);
        }, speed / 50);
    }

    function fadeOut(elem, speed) {
        var outInterval = setInterval(function () {
            if (!elem.style.opacity) {
                elem.style.opacity = 1;
            }
            elem.style.opacity -= 0.02;
            if (elem.style.opacity <= 0)
                clearInterval(outInterval);
        }, speed / 50);
    }

    function focusHandler(evt) {
        evt.preventDefault();
        evt.stopPropagation();
        var length = evt.target.value.length;
        setPositionOne(length);
        setPositionTwo(length);
    }

    function inputHandler(evt) {
        var length = evt.target.value.length;
        setPositionOne(length);
        setPositionTwo(length);
    }

    function setPositionOne(len) {
        if (len < 2) {
            setPosition('First', 56, 110, 101, 111);
        }
        else if (len < 3) {
            setPosition('First', 57, 110, 102, 111);
        }
        else if (len < 4) {
            setPosition('First', 58, 110, 103, 111);
        }
        else if (len < 5) {
            setPosition('First', 59, 110, 104, 111);
        }
        else if (len < 6) {
            setPosition('First', 60, 110, 104, 111);
        }
        else if (len < 7) {
            setPosition('First', 61, 110, 105, 111);
        }
        else if (len < 8) {
            setPosition('First', 62, 110, 106, 111);
        }
        else if (len < 9) {
            setPosition('First', 63, 110, 107, 111);
        }
        else if (len > 12) {
            setPosition('First', 64, 110, 108, 111);
        }
    }

    function setPositionTwo(len) {
        if (len < 2) {
            setPosition('Second', 245, 167, 290, 168);
        }
        else if (len < 3) {
            setPosition('Second', 246, 168, 291, 169);
        }
        else if (len < 4) {
            setPosition('Second', 247, 168, 292, 169);
        }
        else if (len < 5) {
            setPosition('Second', 248, 168, 293, 169);
        }
        else if (len < 6) {
            setPosition('Second', 249, 168, 294, 169);
        }
        else if (len < 7) {
            setPosition('Second', 250, 168, 294, 169);
        }
        else if (len < 8) {
            setPosition('Second', 250, 168, 294, 169);
        }
        else if (len === 11) {
            setPosition('Second', 251, 168, 295, 169);
        }
        else if (len === 12) {
            setPosition('Second', 252, 168, 296, 169);
        }
        else if (len === 13) {
            setPosition('Second', 253, 168, 297, 169);
        }
        else if (len > 13) {
            setPosition('Second', 254, 168, 298, 169);
        }
    }

    function blurHandler() {
        setPosition('First', 58, 107, 104, 108);
        setPosition('Second', 250, 164, 296, 164);
    }

    function clickHandler() {
        var wrapper = document.querySelector('.wrapper');
        inputPassword.type = 'password';
        fadeOut(wrapper, 1000);
    }

    function setPosition(person, xLeft, yLeft, xRight, yRight) {
        eval('eye' + person + 'Left').style.left = xLeft + 'px';
        eval('eye' + person + 'Left').style.top = yLeft + 'px';
        eval('eye' + person + 'Right').style.left = xRight + 'px';
        eval('eye' + person + 'Right').style.top = yRight + 'px';
    }
})();
