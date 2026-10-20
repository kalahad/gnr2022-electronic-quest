  const pin=e.target.closest('#pqChip .pin'); if(pin){pqPick(+pin.dataset.pin);return;}
  if(e.target.closest('#pqSkip')){pqI++;pqAskNext();SFX.play('select');return;}
  if(e.target.closest('#mnTrig')){mnTrig();return;}
  if(e.target.closest('#mnNext')){mnI=(mnI+1)%MN_G.length;SFX.play('select');mnShow();return;}
  if(e.target.closest('#bpNext')){bpI=(bpI+1)%BP_G.length;SFX.play('select');bpUpdate(false);return;}
  if(e.target.closest('#bpSnd')){bpSound=!bpSound;const b=$('#bpSnd');b.textContent=bpSound?'เสียงจังหวะ เปิด':'เสียงจังหวะ ปิด';b.className='toggle '+(bpSound?'on':'off');return;}
