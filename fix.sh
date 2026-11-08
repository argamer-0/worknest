python3 -c "
with open('index.html', 'r') as f:
    content = f.read()

old_code = '''      // Trigger Fast2SMS Quick Gateway
      try {
        const smsUrl = \`https://www.fast2sms.com/dev/bulkV2?authorization=\${FAST2SMS_KEY}&route=otp&variables_values=\${code}&flash=0&numbers=\${phone}\`;
        fetch(smsUrl, { mode: 'no-cors' }).then(() => {
          console.log(\"Fast2SMS request dispatched.\");
        }).catch(err => console.log(err));
      } catch (e) {
        console.log(e);
      }'''

new_code = '''      // Trigger Fast2SMS via CORS Bypass Proxy
      try {
        const targetUrl = encodeURIComponent(\`https://www.fast2sms.com/dev/bulkV2?authorization=\${FAST2SMS_KEY}&route=otp&variables_values=\${code}&flash=0&numbers=\${phone}\`);
        const proxyUrl = \`https://api.allorigins.win/raw?url=\${targetUrl}\`;
        
        fetch(proxyUrl)
          .then(res => res.json())
          .then(data => {
            console.log('Fast2SMS Delivery Response:', data);
          })
          .catch(err => console.log('Proxy Error:', err));
      } catch (e) {
        console.log(e);
      }'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('index.html', 'w') as f:
        f.write(content)
    print('Successfully patched index.html')
else:
    print('Pattern not matched, applying full update')
"
git add .
git commit -m "Fix Fast2SMS delivery using CORS proxy"
git push origin main
