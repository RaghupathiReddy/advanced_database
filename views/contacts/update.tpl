<html>
<body>
<h2>Update Contact</h2>
<hr/>
<form action="/contacts/update" method="post">
  <input type="hidden" name="id" value="{{id}}"/>
  <p>Name: <input name="name" value="{{name}}"/></p>
  <p>Description: <input name="description" value="{{description}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<hr/>
</body>
</html>