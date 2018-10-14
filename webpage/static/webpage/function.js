const nav = document.querySelector('.navbar');
const menu = document.querySelector('.logo button');
const list = document.querySelector('.navbar ul');

menu.addEventListener('click', (e) => {
  if(e.target.className === 'button'){
    list.classList.add('hidden');
    menu.classList.add('active');
  }else{
    list.classList.remove('hidden');
    menu.classList.remove('active');
  }
})
