<html>
<body>
<h2>View Contact</h2>
<hr/>
<p>Name: {{contact.name}}</p>
<p>Description: {{contact.description}}</p>
Accounts
<form action="/add_account_contacts" method="post">
  <input type="hidden" name="contact" value="{{contact.id}}"/>
  <select name="account_id">
  % for account in accounts:
    <option value="{{account.id}}">{{account.name}}</option>
  % end
  </select>
  <button type="submit">Add Account</button>
</form>
<table>
    <tr>
        <th>Name</th>
        <th>Description</th>
    </tr>
    % for account in contact.accounts:
        <tr>
            <td>{{account.name}}</td>
            <td>{{account.description}}</td>
            <td><a href="/update/{{str(account.id)}}">View</a></td>
            <td><a href="/delete/{{str(account.id)}}">Delete</a></td>
        </tr>
    % end
</table>
<hr/>
</body>
</html>