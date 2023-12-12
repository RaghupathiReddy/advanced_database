<html>
  <body>
    <h2>View Account</h2>
    <hr/>
    <p>Name: {{account.name}}</p>
    <p>Description: {{account.description}}</p>
    Contacts
    <form action="/add_account_contacts" method="post">
      <input type="hidden" name="account_id" value="{{account.id}}"/>
      <select name="contact_id">
      % for contact in contacts:
        <option value="{{contact.id}}">{{contact.name}}</option>
      % end
      </select>
      <button type="submit">Add Contact</button>
    </form>
    <table>
        <tr>
          <th>Name</th>
          <th>Description</th>
        </tr>
        % for contact in account.contacts:
          <tr>
            <td>{{contact.name}}</td>
            <td>{{contact.description}}</td>
            <td><a href="/contacts/show/{{str(contact.id)}}">View</a></td>
            <td><a href="/delete_contact_accounts/{{str(account.id)}}/{{str(contact.id)}}">Remove</a></td>
          </tr>
        % end
    </table>
    <hr/>
  </body>
</html>