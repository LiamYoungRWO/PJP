document.addEventListener('keydown', movePlayer);
let player = document.getElementById('player');
let ronin = document.getElementById('ronin');

function movePlayer(e) {
    let playerStyle = window.getComputedStyle(player);
    let playerLeft = parseInt(playerStyle.left);
    let playerTop = parseInt(playerStyle.top);

    if (e.key === 'ArrowLeft' && playerLeft > 0) {
        player.style.left = (playerLeft - 10) + 'px';
    }
    if (e.key === 'ArrowRight' && playerLeft < 550) {
        player.style.left = (playerLeft + 10) + 'px';
    }
    if (e.key === 'ArrowUp' && playerTop > 0) {
        player.style.top = (playerTop - 10) + 'px';
    }
    if (e.key === 'ArrowDown' && playerTop < 350) {
        player.style.top = (playerTop + 10) + 'px';
    }
    
    checkCollision();
}

function checkCollision() {
    let playerRect = player.getBoundingClientRect();
    let roninRect = ronin.getBoundingClientRect();
    
    if (playerRect.x < roninRect.x + roninRect.width &&
        playerRect.x + playerRect.width > roninRect.x &&
        playerRect.y < roninRect.y + roninRect.height &&
        playerRect.y + playerRect.height > roninRect.y) {
            alert("Battle with Ronin!");
            resetPositions();
    }
}

function resetPositions() {
    player.style.left = '0px';
    player.style.top = '0px';
}
