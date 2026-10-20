  if(e.target.closest('#gnNext')){gnI=(gnI+1)%GN_T.length;SFX.play('select');gnUpdate(false);return;}
  const dp=e.target.closest('[data-db]'); if(dp){dbPick(+dp.dataset.db);return;}
  if(e.target.closest('#dbNext')){dbI=(dbI+1)%DB.length;SFX.play('select');dbRender();return;}
