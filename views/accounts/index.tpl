<html>
<body>
<h2>Accounts</h2>
<hr/>
<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
% for account in accounts:
  <tr>
    <td>{{account.name}}</td>
    <td>{{account.description}}</td>
    <td><a href="/show/{{str(account.id)}}">Show</a></td>
    <td><a href="/update/{{str(account.id)}}">Update</a></td>
    <td><a href="/delete/{{str(account.id)}}">Delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add new item</a>
</body>
</html>