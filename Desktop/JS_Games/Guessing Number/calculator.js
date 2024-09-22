'using strict';
  
/*
console.log(document.querySelector(".message").textContent);
document.querySelector(".message").textContent = prompt('Put in any word');
console.log(document.querySelector('.message').value);
document.querySelector('.message1').value = 13; */
let number = Math.trunc(Math.random() * 20) + 1;
document.querySelector('.message').textContent = number;

let score = document.querySelector('.score').textContent;

let highScore = 0;


document.querySelector('.btn').addEventListener('click', function(){
  const x = Number(document.querySelector('.message1').value);
 
  if(!x){
  document.querySelector('.result').textContent = 'No Number!';
  }
  else if(x === number){
    document.querySelector('.result').textContent = 'You Win';
    if(score > highScore){
      highScore = score;
      document.querySelector('.highScore').textContent = highScore;
    }
    else if(score === 0){
      document.querySelector('.result').textContent = 'You lost the game!';
    }
    document.querySelector('body').style.backgroundColor = 'green';
  }
  else if(x > number){
    if(score > 0){
      document.querySelector('.result').textContent = 'too high';
      score = score - 1;
      document.querySelector('.score').textContent = score;
    }
    else{
      document.querySelector('.result').textContent = 'You lost the game!';
    }
    document.querySelector('yourChoice').textContent = x;
  }
  else if(x < number){
    if(score > 0){
      document.querySelector('.result').textContent = 'too low';
      score = score - 1;
      document.querySelector('.score').textContent = score;
    }

    else{
      document.querySelector('.result').textContent = 'You lost the game!';
    }
 
  }

});
document.querySelector('.resetBtn').addEventListener('click', function(){ 
  number = Math.trunc(Math.random() * 20) + 1;
  document.querySelector('.message').textContent = number;
  document.querySelector('.score').textContent = 20;
  score = 20;
  document.querySelector('.result').textContent = 'start guessing';
  document.querySelector('.message1').value = '';
});


