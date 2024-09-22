'using stric';

let yourScore = 0;
let aiScore = 0;
let drawScore = 0;
let highScore = 0;
document.querySelector('.rst').addEventListener('click', function(){
    document.querySelector('.yourScore').textContent = 0;
    document.querySelector('.aiScore').textContent = 0;
    document.querySelector('.drawScore').textContent = 0;
});
//ROCK = 0 ; PAPER = 1; SCISSOR = 2;

//ROCK
document.querySelector('.btn0').addEventListener('click', function(){
    let randomIntegerInRange = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
    let ai = randomIntegerInRange(0, 2);

    console.log(ai);
    if(ai === 0){
        document.querySelector('.status').textContent = "IT'S A DRAW";
        drawScore++;
        document.querySelector('.drawScore').textContent = drawScore;
    }
    else if(ai === 1){
        document.querySelector('.status').textContent = 'You win!';
        yourScore++;
        document.querySelector('.yourScore').textContent = yourScore;
        if(yourScore > highScore){
            highScore = yourScore;
            document.querySelector('.highScore').textContent = highScore;
        }
    }
    else if(ai === 2){
        document.querySelector('.status').textContent = 'YOU LOSE';
        aiScore++;
        document.querySelector('.aiScore').textContent = aiScore;
    }
});

//PAPER
document.querySelector('.btn1').addEventListener('click', function(){
    let randomIntegerInRange = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
    let ai = randomIntegerInRange(0, 2);

    console.log(ai);
    if(ai === 0){
        document.querySelector('.status').textContent = "YOU WIN";
        yourScore++;
        document.querySelector('.yourScore').textContent = yourScore;
        if(yourScore > highScore){
            highScore = yourScore;
            document.querySelector('.highScore').textContent = highScore;
        }
    }
    else if(ai === 1){
        document.querySelector('.status').textContent = "IT'S A DRAW";
        drawScore++;
        document.querySelector('.drawScore').textContent = drawScore;
    }
    else if(ai === 2){
        document.querySelector('.status').textContent = 'YOU LOSE';
        aiScore++;
        document.querySelector('.aiScore').textContent = aiScore;
    }
});

//Scissor
document.querySelector('.btn2').addEventListener('click', function(){
    let randomIntegerInRange = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
    let ai = randomIntegerInRange(0, 2);

    console.log(ai);
    if(ai === 0){
        document.querySelector('.status').textContent = 'YOU LOSE';
        aiScore++;
        document.querySelector('.aiScore').textContent = aiScore;
    }
    else if(ai === 1){
        document.querySelector('.status').textContent = "YOU WIN";
        yourScore++;
        document.querySelector('.yourScore').textContent = yourScore;
        if(yourScore > highScore){
            highScore = yourScore;
            document.querySelector('.highScore').textContent = highScore;
        }
    }
    else if(ai === 2){
        document.querySelector('.status').textContent = "IT'S A DRAW";
        drawScore++;
        document.querySelector('.drawScore').textContent = drawScore;
    }
});

