'use struct';
let score = 0;
let bombBtn = 0;

const container = document.querySelectorAll('.cont');

const yourScore = document.querySelector('.yourScore');
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');

const clicked = 0;
let arr = [];

for(let x = 0; x <= container.length; x++){


  container[x].addEventListener('click', function(){
    

    if(arr.includes(container[x])){
    
    }
    else{
      arr.push(container[x]);
      const num = Math.trunc(Math.random() * 2);

        if(num === 1){

          document.getElementById(`conts${x}`).textContent  = num;
          score++;
          console.log(arr);
        }

        else if(num === 0){

        document.getElementById(`conts${x}`).style.backgroundImage  = "url('bomb.png')";
        console.log(arr);
        bombBtn++;  

            if(bombBtn === 5){
              console.log('game is over');
              yourScore.textContent =  score;
              modal.classList.remove('hidden');
              overlay.classList.remove('hidden');

            }

        }
    }

  });

  document.querySelector('.btnClose').addEventListener('click', function(){

    yourScore.textContent = '';
    modal.classList.add('hidden');
    overlay.classList.add('hidden');   
    location.reload();

  });
}
