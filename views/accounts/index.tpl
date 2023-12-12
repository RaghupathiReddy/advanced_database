<html>
  <body>
    <h2>Accounts</h2>
    <hr/>
    <div>
      <form action="/" method="get">
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