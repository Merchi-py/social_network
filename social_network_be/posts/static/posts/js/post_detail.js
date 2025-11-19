function DropdownList(btn){
    let menu = btn.nextElementSibling; // take next element
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block'; // if else  Examination and rewrite old value to new
}

// Closing menu, when user clicked somewhere but not into the block
window.onclick = (e) => {
    // If user hasn't clicked on the button, of options
    if (!e.target.matches('.menu-btn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            dropdowns[i].style.display = 'none';
        } // for cycle for closing each button
    }
}

function deletePost(btn){
    let res = confirm('Are you sure?');

    if (res) {
        let form = document.getElementById('deleteForm');
        form.submit();
    }
}