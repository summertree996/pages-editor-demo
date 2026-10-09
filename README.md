# Homepage editing demonstration

A minimal working example that keeps editing, content storage, builds and hosting within GitHub. The editing form is GitHub's native issue form, rather than a separate CMS administration page.

- [Published homepage](https://summertree996.github.io/pages-editor-demo/)
- [Edit homepage text](https://github.com/summertree996/pages-editor-demo/issues/new?template=update-homepage.yml)
- [Publication progress](https://github.com/summertree996/pages-editor-demo/actions)

Open the editing form, fill in the new homepage text, and submit. GitHub Actions saves the text to `data/content.json`, generates the static page, and deploys it through GitHub Pages. The form submission must be made by the repository owner. Other users' submissions cannot update the website.

The demonstration changes one text field. It does not modify the separate Ran Wei academic website. Adding a full biography, publications, courses and photo editor would require additional content forms and editing behavior.

Build locally with `python scripts/build.py`. On GitHub, Pages must use GitHub Actions as its publishing source. No external login service, personal access token or cloud-provider account is needed for the editor.
