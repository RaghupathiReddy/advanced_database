<html>
  <body>
    <h2>Contacts</h2>
    <hr/>
    <div>
      <form action="/contacts" method="get">
        <label for="search">Search</label>
        <input type="text" id="search" name="q" value="{{query}}"></input>
        <button type="search">Search</button>
      </form>
    </div>
    <table>
      <tr>
        <th>Name</th>
        <th>Description</th>
      </tr>
      % for contact in contacts:
        <tr>
          <td>{{contact.name}}</td>
          <td>{{contact.description}}</td>
          <td><a href="/contacts/show/{{str(contact.id)}}">show</a></td>
          <td><a href="/contacts/update/{{str(contact.id)}}">update</a></td>
          <td><a href="/contacts/delete/{{str(contact.id)}}">delete</a></td>
        </tr>
      % end
    </table>
    <hr/>
    <a href="/contacts/new">Add new item</a>
  </body>
</html>