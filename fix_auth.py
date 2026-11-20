with open("index.html", "r", encoding="utf-8") as f:
    code = f.read()

# Local cache check before showing setup screen so returning users never see form again
old_check = '''const { data: profile } = await sb
        .from('profiles')
        .select('*')
        .eq('id', authUser.id)
        .maybeSingle();'''

new_check = '''const cachedProf = JSON.parse(localStorage.getItem('wn_prof_' + authUser.id) || 'null');
      if (cachedProf && cachedProf.phone) {
        openDashboard(cachedProf);
        return;
      }
      const { data: profile } = await sb
        .from('profiles')
        .select('*')
        .eq('id', authUser.id)
        .maybeSingle();
      if (profile && profile.phone) {
        localStorage.setItem('wn_prof_' + authUser.id, JSON.stringify(profile));
      }'''

code = code.replace(old_check, new_check)

# Save local cache on form submit
old_open = '''openDashboard(data || { full_name: name, phone: phone, gov_id: govid, uid_code: customUID });'''
new_open = '''const finalProf = data || { full_name: name, phone: phone, gov_id: govid, uid_code: customUID };
      localStorage.setItem('wn_prof_' + authUser.id, JSON.stringify(finalProf));
      openDashboard(finalProf);'''

code = code.replace(old_open, new_open)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(code)
