% import model
% rebase('views/base.tpl')


  <h1>Kalkulator kalorij</h1>

  <blockquote>
    Izračunajmo predvideno oceno tvojega dnevnega vnosa kalorij.
  </blockquote>
  <p>Vpišite podatke in izračunajte, koliko energije porabite dnevno za vzdrževanje svoje telesne teže pri svojih navadah oz. fizičnih aktivnostih.</p>
  <div style="background-color: #ffffcc; padding: 20px;">
  <form method="post" name="test">
  <h4>Vaša starost</h4> 
  <input style="width: 50px; display: inline-block;" name="starost" size="3" type="text" /> let
  <h4>Vaša višina</h4> 
  <input style="width: 50px; display: inline-block;" name="visina" size="3" type="text" /> cm
  <h4>Vaša masa</h4> 
  <input style="width: 50px; display: inline-block;" name="teza" size="3" type="text" /> kg
  <h4>Spol</h4>
  <label for="s1"><input id="s1" name="spol" type="radio" value="Z" />ženska</label><br> <label for="s2"><input id="s2" name="spol" type="radio" value="M" />moški</label>
  <h4>Vaša aktivnost</h4> 
  <label for="a1"><input id="a1" name="aktivnost" type="radio" value="1.2" />Brez aktivnosti</label><br> <label for="a2"><input id="a2" name="aktivnost" type="radio" value="1.375" />Zelo malo aktivnosti (1-3 dni na teden)</label><br> <label for="a3"><input id="a3" name="aktivnost" type="radio" value="1.55" />Zmerna aktivnost (3-5 dni na teden)</label><br> <label for="a4"><input id="a4" name="aktivnost" type="radio" value="1.725" />Visoka stopnja aktivnosti (6-7 dni na teden)</label><br> <label for="a5"><input id="a5" name="aktivnost" type="radio" value="1.9" />Zelo visoka stopnja aktivnosti (2× na dan, zelo težki treningi)</label><p><input type="button" value="Izračunaj" 

   % end
   
  <img src="img/10.jpg" alt="obesanje">

  <form action="/igra/" method="post">
    <button type="submit">Nov izračun</button>
  </form>
