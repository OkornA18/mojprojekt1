% import model
% rebase('views/base.tpl')

  <p>
  Izračunajmo predvideno oceno tvojega dnevnega vnosa kalorij.
  </p>

  <p>
  Vpišite svoje podatke in izračunajte, koliko energije potrebujete dnevno za vzdrževanje, pridobitev ali izgubo svoje telesne teže pri svojih navadah oz. fizičnih aktivnostih.</p>
  <div style="background-color: #ffffcc; padding: 20px;">
  <form method="post" name="test">

  <p>
  <form action="/igra/" method="post">
    <p><tr><td>Vaša starost v letih: <input type='text' name='starost' pattern="[0-9]{1,}" title="Napaka"> (npr: 17) </td></tr>

    <p><tr><td>Vaša višina v centimetrih: <input type='text' name='visina' pattern="[0-9]{2,}" title="Napaka"> (npr: 175) </td></tr>

    <p><tr><td>Vaša masa v kilogramih: <input type='text' name='masa' pattern="[0-9]{2,}" title="Napaka"> (npr: 50) </td></tr>

  <h4>Spol</h4>
    <label for="s1">
      <input id="s1" name="spol" type="radio" value="Z" required />ženska
    </label><br> 
    <label for="s2">
      <input id="s2" name="spol" type="radio" value="M" />moški
    </label>

    <h4>Vaša aktivnost - izberite možnost, ki najbolje opisuje vašo športno aktivnost v enem povprečnem tednu.</h4> 
    <label for="a1">
      <input id="a1" name="aktivnost" type="radio" value="1.2" required />Brez aktivnosti
    </label><br> 

    <label for="a2">
      <input id="a2" name="aktivnost" type="radio" value="1.375" />Zelo malo aktivnosti (1-3 dni na teden)
    </label><br> 

    <label for="a3">
      <input id="a3" name="aktivnost" type="radio" value="1.55" />Zmerna aktivnost (3-5 dni na teden)
    </label><br> 

    <label for="a4">
      <input id="a4" name="aktivnost" type="radio" value="1.725" />Visoka stopnja aktivnosti (6-7 dni na teden)
    </label><br>

    <label for="a5">
      <input id="a5" name="aktivnost" type="radio" value="1.9" />Zelo visoka stopnja aktivnosti (2× na dan, zelo težki treningi)
    </label>
    
    <p><button type="submit">Izračunaj</button>
  </form>

<h2> Rezultati </h2>
  <h4> Vrednost vašega bazalnega metabolizma (BMR): {{kalorije.bmr()}} </h4>

  <h4> Spodaj je tabela, ki prikazuje, koliko kalorij na dan bi morali zaužiti, da bi se vaša telesa masa ohranila ali pa spremenila po vaših željah. </h4>

  
  <table style="width:30%">
    <tr>
      <th> ŽELJA </th>
      <th> KALORIJE/DAN </th>
    </tr>
    <tr>
      <th> vzdrževati telesno težo </th>
      <th> {{kalorije.vzdrzevanje()}} </th>
    </tr> 
    <tr>
      <th> pridobiti telesno težo </th>
      <th> {{kalorije.pridobitev()}} </th>
    </tr> 
    <tr>
      <th> izgubiti telesno težos </th>
      <th> {{kalorije.izguba()}} </th>
    </tr> 
  </table>