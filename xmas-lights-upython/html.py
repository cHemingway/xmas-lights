def generate_html(patterns_json):
    return '''<!DOCTYPE html><html lang=en><head><meta charset=UTF-8><title>Xmas Lights</title><link href=https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css rel=stylesheet integrity=sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65 crossorigin=anonymous><link rel=stylesheet href=https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.2/font/bootstrap-icons.css><script src=https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js integrity=sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4 crossorigin=anonymous></script><link rel=stylesheet data-name=vs/editor/editor.main href=https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.34.1/min/vs/editor/editor.main.min.css><link href="https://fonts.googleapis.com/css?family=Oswald" rel=stylesheet type=text/css><style>.error-tooltip{--bs-tooltip-bg:var(--bs-red);--bs-tooltip-max-width:500px;--bs-tooltip-opacity:100}.tooltip-inner{text-align:left}.editButton{border:none;background:0 0;margin:0;padding:0;color:#1e90ff;visibility:hidden}.editButton:hover{color:#06f}.buttonParent:hover .editButton{visibility:visible}.deleteButton{border:none;background:0 0;margin:0;padding:0 0 0 10px;color:#cd5c5c;visibility:hidden}.deleteButton:hover{color:red}.buttonParent:hover .deleteButton{visibility:visible}.activeDiv{display:flex;justify-content:left}.errorButton{border:none;background:0 0;margin:0;padding:0 4px 0 0;color:var(--bs-red);cursor:default!important}.activeButton{border:none;background:0 0;margin:0;padding:0;color:gray;visibility:hidden;alignment:right}.activeButton .bi-stop-fill{display:none;color:#464646}.activeButton.active{visibility:visible;color:#464646}.activeButton.active:hover .bi-stop-fill{display:inline-block;visibility:visible;color:#464646}.activeButton.active:hover .bi-play-fill{display:none;color:#464646}.activeButton:hover{color:#464646}.buttonParent:hover .activeButton{visibility:visible}.main-title{font-family:Oswald,sans-serif;font-style:italic;text-align:center;font-size:500%;text-shadow:3px 2px red,5px 4px #0f0;color:#00f}body{background:#fff4f4}table{color:#464646!important}#addButton{border:none;background:0 0;padding:0;color:gray;margin:-20px auto 0;font-size:40px}#addButton:hover{color:#464646}</style></head><body><h1 class=main-title>XMAS LIGHTS</h1><table style=width:auto;min-width:500px;margin-left:auto;margin-right:auto class="table table-hover"><thead><tr><th>Status</th><th>Pattern Name</th><th>Author</th><th>Actions</th></tr></thead><tbody id=patternsTable></tbody></table><div style=display:flex><button id=addButton type=button onclick=editPattern(null)>+</button></div><div class="modal fade" id=editPatternModal tabindex=-1><div class="modal-dialog modal-lg"><div class=modal-content><div class=modal-header><h1 class="modal-title fs-5" id=editPatternModalLabel>Edit pattern</h1><button type=button class=btn-close data-bs-dismiss=modal aria-label=Close></button></div><div class=modal-body><form><div class=form-group><label for=editPatternName>Pattern name:</label> <input class=form-control id=editPatternName type=text></div><br><div class=form-group><label for=editPatternAuthor>Author:</label> <input class=form-control id=editPatternAuthor type=text></div><br><div class=form-group><label for=monaco-editor-container>Code:</label><div id=monaco-editor-container style="height:400px;border:1px solid #000"></div></div></form></div><div class=modal-footer><button type=button class="btn btn-secondary" data-bs-dismiss=modal>Close</button> <button type=button class="btn btn-primary" id=saveButton>Save changes</button></div></div></div></div><script type=text/javascript src=https://unpkg.com/monaco-editor@latest/min/vs/loader.js></script><script>require.config({paths:{vs:"https://unpkg.com/monaco-editor@latest/min/vs"}}),window.MonacoEnvironment={getWorkerUrl:function(t,o){return"data:text/javascript;charset=utf-8,"+encodeURIComponent("self.MonacoEnvironment = {"`baseUrl: 'https://unpkg.com/monaco-editor@latest/min/'``};``importScripts('https://unpkg.com/monaco-editor@latest/min/vs/base/worker/workerMain.js');`)}}</script><script>const myModal=new bootstrap.Modal(document.getElementById("editPatternModal"),{}),editPatternName=document.getElementById("editPatternName"),editPatternAuthor=document.getElementById("editPatternAuthor");let monacoEditor=null;function escapeHtml(e){return e.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#039;")}function editPattern(t){require(["vs/editor/editor.main"],function(){null===monacoEditor&&(monacoEditor=monaco.editor.create(document.getElementById("monaco-editor-container"),{value:"placeholder",language:"python",theme:"vs-dark",minimap:{enabled:!1},automaticLayout:!0,lineNumbersMinChars:3})),null===t?monacoEditor.setValue(`# Parameters:
#   led_index: current LED
#   max_leds: LEDs in the string
#   time_seconds: current time as a float (starts at 0.0)
#
# Output:
#   Put list of [R, G, B] values into variable \`result\`
#   Values mut be between 0 and 255

result = [
  255 * (time_seconds + led_index)/max_leds,
  180 * (time_seconds + led_index)/max_leds,
  123 * (time_seconds + led_index)/max_leds,
]
`):(editPatternName.value=patterns[t].name,editPatternAuthor.value=patterns[t].author,monacoEditor.setValue(patterns[t].script))}),myModal.show(),document.getElementById("saveButton").onclick=()=>{const e=new XMLHttpRequest;e.open("POST","/",!0),e.setRequestHeader("Content-Type","application/json"),e.onreadystatechange=()=>{e.readyState===XMLHttpRequest.DONE&&200===e.status&&location.reload()},e.send(JSON.stringify({id:t,name:editPatternName.value,author:editPatternAuthor.value,script:monacoEditor.getValue(),active:null!==t&&patterns[t].active}))}}patternsJson=''' + patterns_json + ''';let patterns=JSON.parse(patternsJson);const table=document.getElementById("patternsTable");for(const[d,e]of Object.entries(patterns)){let t=document.createElement("tr"),a=document.createElement("td"),n=(a.className="activeTd",document.createElement("button")),o=(n.innerHTML='<h6 style="margin: 0"><i class="bi bi-exclamation-circle"></i></h6>',n.className="errorButton",document.createElement("div")),r=(o.className="activeDiv",document.createElement("button")),i=(r.innerHTML='<h5 style="margin: 0"><i class="bi bi-play-fill"></i><i class="bi bi-stop-fill"></i></h5>',r.type="button",r.className="activeButton",r.onclick=()=>{const t=new XMLHttpRequest;t.open("POST","/",!0),t.setRequestHeader("Content-Type","application/json"),t.onreadystatechange=()=>{t.readyState===XMLHttpRequest.DONE&&200===t.status&&location.reload()},t.send(JSON.stringify({id:d,active:!e.active}))},e.active&&r.classList.add("active"),e.hasOwnProperty("error")&&null!==e.error?(n.setAttribute("data-bs-title",escapeHtml(e.error).replaceAll("\\n","<br>")),n.setAttribute("data-bs-toggle","tooltip"),n.setAttribute("data-bs-placement","bottom"),n.setAttribute("data-bs-custom-class","error-tooltip"),n.setAttribute("data-bs-html","true")):n.setAttribute("style","visibility: hidden"),o.appendChild(n),o.appendChild(r),a.appendChild(o),t.appendChild(a),document.createElement("td")),l=(i.innerText=e.name,t.appendChild(i),document.createElement("td")),s=(l.innerText=e.author,t.appendChild(l),document.createElement("td")),c=document.createElement("button"),u=(c.innerText="Edit",c.type="button",c.className="editButton",c.onclick=()=>{editPattern(d)},document.createElement("button"));u.innerText="Delete",u.type="button",u.className="deleteButton",u.onclick=()=>{const e=new XMLHttpRequest;e.open("DELETE","/",!0),e.setRequestHeader("Content-Type","application/json"),e.onreadystatechange=()=>{e.readyState===XMLHttpRequest.DONE&&200===e.status&&location.reload()},e.send(JSON.stringify({id:d}))},s.appendChild(c),s.appendChild(u),t.appendChild(s),t.className="buttonParent",table.appendChild(t);const p=document.querySelectorAll('[data-bs-toggle="tooltip"]'),q=[...p].map(e=>new bootstrap.Tooltip(e))}</script></body></html>'''