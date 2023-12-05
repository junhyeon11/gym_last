document.addEventListener('DOMContentLoaded', () => {
    const navbar__menu = document.querySelector('.navbar__menu');
    const login_button = document.querySelector('.login_button');
    const user_data = document.querySelector('.userdata')
    const logo = document.querySelector('.navbar__logo')
    window.addEventListener('scroll', () => {
        if (window.scrollY >= 100) {
            navbar__menu.classList.add('blind_css');
            if (login_button) {
                login_button.classList.add('blind_css');
            }
            if (user_data) {
                user_data.classList.add('blind_css');
            }
            logo.classList.add('logo_mid')
        } else {
            navbar__menu.classList.remove('blind_css');
            if (login_button) {
                login_button.classList.remove('blind_css');
            }
            if (user_data) {
                user_data.classList.remove('blind_css');
            }
            logo.classList.remove('logo_mid')

        }
    });

    const navbars = document.getElementById('navbar')

    navbars.addEventListener('mouseenter', function() {
        logo.classList.remove('logo_mid')

        navbar__menu.classList.remove('blind_css');
        if (login_button) {
            login_button.classList.remove('blind_css');
        }
        if (user_data) {
            user_data.classList.remove('blind_css');
        }
    })

    navbars.addEventListener('mouseleave', function() {
        logo.classList.add('logo_mid')

        navbar__menu.classList.add('blind_css');
        if (login_button) {
            login_button.classList.add('blind_css');
        }
        if (user_data) {
            user_data.classList.add('blind_css');
        }
    })

    const mypase_iframe = document.querySelector('.mypase_iframe');
    const mypase_small = document.querySelector('.mypase_small')
    user_data.addEventListener('mouseenter', function() {
        mypase_iframe.style.display = 'block'
    })
    mypase_small.addEventListener('mouseleave', function() {
        mypase_iframe.style.display = 'none'
    })
});