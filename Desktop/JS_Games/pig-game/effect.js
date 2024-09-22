const btnNewGame = document.querySelector('.btnNewGame');
const player0El = document.querySelector('.player0');
const player1El= document.querySelector('.player1');
const btnRoll = document.querySelector('.btnRoll');
const btnHold = document.querySelector('.btnHold');
const diceEl = document.querySelector('.dice-img');
const modal0 = document.querySelector('.modal0');
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const player0Score = document.querySelector('.player0rScore');
const player1Score = document.querySelector('.player1rScore');
const score0 = document.querySelector('.scorepl0');
const score1 = document.querySelector('.scorepl1');
const close0 = document.querySelector('.close0');
const close = document.querySelector('.close');
const score = [0 , 0];
const hScore = [0, 0];

let activePlayer = 0;


btnNewGame.addEventListener('click', function(){
    diceEl.classList.add('hidden');
    player0Score.textContent = 0;
    player1Score.textContent = 0;
    score0.textContent = 0;
    score1.textContent = 0;
    score[0] = 0;
    score[1] = 0;
    hScore[0] = 0;
    hScore[1] = 0;

    document.querySelector('.pNum').textContent = '';
    document.querySelector('.pScore').textContent = 0;
    player0El.classList.add('active');
    player1El.classList.remove('active');
    modal0.classList.remove('hidden');
    overlay.classList.remove('hidden');

});


btnRoll.addEventListener('click', function(){
    diceEl.classList.remove('hidden');
    const dice = Math.trunc(Math.random() * 6) + 1;
    diceEl.src = `dice${dice}.png`;
    if(dice === 1){
        score[activePlayer] = 0;
        hScore[activePlayer] = 0;
        document.querySelector(`.player${activePlayer}rScore`).textContent = 0;
        document.querySelector(`.scorepl${activePlayer}`).textContent = 0;
        activePlayer = activePlayer === 0 ? 1 : 0;
        player0El.classList.toggle('active');
        player1El.classList.toggle('active');

        
    }else{
        score[activePlayer] += dice;
        document.querySelector(`.player${activePlayer}rScore`).textContent = score[activePlayer];
    }
    
});

btnHold.addEventListener('click', function(){
    document.querySelector(`.player${activePlayer}rScore`).textContent = 0;
    hScore[activePlayer] += score[activePlayer];

    document.querySelector(`.scorepl${activePlayer}`).textContent = hScore[activePlayer]; 
    

    if(hScore[0] >= 20){
    
        modal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        document.querySelector('.pNum').textContent = 1;
        document.querySelector('.pScore').textContent = hScore[activePlayer];
        document.querySelector('.pScore').textContent = hScore[activePlayer];
        document.querySelector('.close').focus();
    
    }
    else if(hScore[1] >= 20){
        
        modal.classList.remove('hidden');
        overlay.classList.remove('hidden');
        document.querySelector('.pNum').textContent = 2;
        document.querySelector('.pScore').textContent = hScore[activePlayer];
        document.querySelector('.close').focus();
    
    }

    score[activePlayer] = 0;

    activePlayer = activePlayer === 0 ? 1 : 0;
    player0El.classList.toggle('active');
    player1El.classList.toggle('active');
    document.querySelector(`.player${activePlayer}rScore`).textContent = 0;
   
});


close.addEventListener('click', function(){
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
    diceEl.classList.add('hidden');

    document.querySelector('.pNum').textContent = '';
    document.querySelector('.pScore').textContent = 0;

    player0Score.textContent = 0;
    player1Score.textContent = 0;
    score0.textContent = 0;
    score1.textContent = 0;
    score[0] = 0;
    score[1] = 0;
    hScore[0] = 0;
    hScore[1] = 0;
});
close0.addEventListener('click', function(){
    modal0.classList.add('hidden');
    overlay.classList.add('hidden');
});
document.addEventListener('keydown', function(e){
    modal0.classList.add('hidden');
    overlay.classList.add('hidden');
});
