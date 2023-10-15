# Create table 'tblTest' 
https://newsimland.com/~todd/JSON/?tok={"tok":"MY_TOKEN","cmd":{"CREATE":"tblTest","EXAMPLE":{"PersonID  PK":"Todd","Score":21}}}

# Store records table
https://newsimland.com/~todd/JSON/?tok={"tok":"MY_TOKEN","cmd":{"STORE":"tblTest","VALUE":[{"PersonID":"Todd","Score":21},{"PersonID":"Jane","Score":2000}]}}

# Retrieve all records in a table
https://newsimland.com/~todd/JSON/?tok={"tok":"MY_TOKEN","cmd":{"ALL":"tblTest"}} 

# Retrieve records in a table with where clause
https://newsimland.com/~todd/JSON/?tok={"tok":"MY_TOKEN","cmd":{"SELECT":"tblTest","WHERE":"Score > 200"}}

# Delete records in a table
https://newsimland.com/~todd/JSON/?tok={"tok":"MY_TOKEN","cmd":{"DELETE":"tblTest","WHERE":"PersonID = 'Jane'"}}

# Update a record in a table

https://newsimland.com/~todd/JSON/?tok={"tok":"MY_TOKEN","cmd":{"STORE":"tblTest","VALUE":[{"PersonID":"Todd","Score":3000}]}}

3.8 Drop the table called tblTest

https://newsimland.com/~todd/JSON/?tok={"tok":"MY_TOKEN","cmd":{"DROP":"tblTest"}}

# I have chosen to use Thunder CLient (VS Code extension) however other tools like Postman could be used
# All requests must be made using the GET method