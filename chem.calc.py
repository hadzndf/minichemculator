import streamlit as st

st.set_page_config(
    page_title="Mini Chemculator",
    page_icon='🧪',
    layout='centered'
)

st.markdown('''
<style>
.stApp {
    background-color: #D4C4EC;
}
h1 {
    color: #95OOFF !important;
    text-align:center;
    font-family: Georgia
}
.welcome-box {
    background-color: #BCA4E3; !important;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px
}
.welcome-box h2 {
    color: #95OOFF; !important;
    font-size: 26px
    font-family: Georgia
}
.welcome-box p {
    color: #9370DB; !important;
    font-size: 16px
}
</style>
''', unsafe_allow_html=True)

st.markdown('''
<div class="welcome-box">
    <h2>Welcome!</h2>
    <p>
        Calculate chemical quantities (for grades 10-11-12)
        through a simple and interactive process.
    </p>
</div>
''', unsafe_allow_html=True)

st.title('Chemculator', text_alignment='center')
st.markdown("""
<p style='text-align: center; color: #9370DB ; font-size: 14px;'>
Created by Hadi Naddaf
</p>""",
unsafe_allow_html=True
)
quantity = st.selectbox('Select quantity you want to calculate', (
    'Number of moles (n)',
    'Mass (m)',
    'Molar Mass of a particle (M)',
    'Volume of the body (V)',
    'Volume of a solution (Vs)',
    'Mass concentration (Cm)',
    'Molar concentration (CM)',
    'Volumic mass / Density (ρ)',
    'Number of particles (x)' ),
                        index=None,
                        placeholder='Select quantity you want to calculate',
                        )


if quantity is not None:



    if quantity == 'Number of moles (n)':
        method_n = st.selectbox('Select the data set that you have',
        ('m & M  (Body mass & Molar mass)',
        'CM & Vs  (Molar concentration of a solution & Total volume of that solution)',
        'x  (Number of particles in the body)',
        'ρ, V & M  (Volumic mass / Density, Volume & Molar mass of the same body)',
        'Cm, Vs & M  (Mass concentration & total volume of a solution, plus the molar mass of solute)',
         'IF GAS: V (Gas volume)'),
                                index=None,
                                placeholder='Select the data set that you have',
        )
        print(''' Choose the method based on the data you have
        If you don't know the molar mass but do know the molecular formula,
        please consult "Molar Mass of a particle (M)"''')


        if method_n is not None:


            if method_n == 'm & M  (Body mass & Molar mass)':
                m_n = st.number_input('Body mass (g)',
                                 min_value=0.0,)
                M_n = st.number_input('Molar mass (g/mol)',
                                       min_value=0.0,)
                if st.button('Calculate number of moles'):
                    if M_n == 0:
                        st.error('Number of moles cannot be calculated (Molar mass should be non-zero)')
                    else:
                        n = m_n / M_n
                        st.success(f"Number of moles = {n} mol")


            elif method_n == 'CM & Vs  (Molar concentration of a solution & Total volume of that solution)':
                CM_n = st.number_input('Molar concentration (mol/L)',
                               min_value=0.0,)
                Vs_n = st.number_input('Total volume of solution (L)',
                               min_value=0.0,)
                if st.button('Calculate number of moles'):
                    if Vs_n == 0:
                        st.error('Number of moles cannot be calculated (Volume should be non-zero)')
                    else:
                        n = CM_n * Vs_n
                        st.success(f"Number of moles = {n} mol")


            elif method_n == 'x  (Number of particles in the body)':
                x_n = st.number_input('Number of particles',
                              min_value=0.0,)
                if st.button('Calculate number of moles'):
                    n = x_n / 6.02e23
                    st.success(f"Number of moles = {n} mol")


            elif method_n == 'ρ, V & M  (Volumic mass / Density, Volume & Molar mass of the same body)':
                p_n = st.number_input('Volumic mass / Density (g/cm³)',
                              min_value=0.0,)
                V_n = st.number_input('Body volume (mL)',
                              min_value=0.0,)
                M_n = st.number_input('Molar mass (g)',
                              min_value=0.0,)
                if st.button('Calculate number of moles'):
                    if M_n == 0:
                        st.error('Number of moles cannot be calculated (Molar mass should be non-zero)')
                    else:
                        n = ( p_n * V_n ) / M_n
                        st.success(f"Number of moles = {n} mol")


            elif method_n == 'Cm, Vs & M  (Mass concentration & total volume of a solution, plus the molar mass of solute)':
                Cm_n = st.number_input('Mass concentration (g/L)',
                              min_value=0.0, )
                Vs_n = st.number_input('Total volume of solution (L)',
                              min_value=0.0, )
                M_n = st.number_input('Molar mass (g)',
                              min_value=0.0, )
                if st.button('Calculate number of moles'):
                    if M_n == 0:
                        st.error('Number of moles cannot be calculated (Molar mass should be non-zero)')
                    else:
                        n = (Cm_n * Vs_n) / M_n
                        st.success(f"Number of moles = {n} mol")


            elif method_n == 'IF GAS: V (Gas volume)':
                V_n = st.number_input('Gas volume (L)',
                              min_value=0.0, )
                if st.button('Calculate interval of number of moles'):
                    n1 = 22.2 * V_n
                    n2 = 24 * V_n
                    st.success(f"Number of moles between {n1} and {n2} mol (depending on room conditions)")



    elif quantity == 'Mass (m)':

        method_m = st.selectbox('Please select the data set that you have',
                            ('n & M  (Number of moles & Molar mass)',
        'Cm & Vs  (Mass concentration of a solution & Total volume of that solution)',
        'x & M  (Number of particles in the body & Molar mass)',
        'ρ & V  (Volumic mass / Density & Volume of the body)',
        'CM, Vs & M  (Molar concentration & total volume of a solution, plus the molar mass of solute)',
        'IF GAS: V & M (Gas volume & Molar mass of gas)'),
                                index=None,
                                placeholder='Select the data set that you have',
                             )
        print(''' Choose the method based on the data you have
        If you don't know the molar mass but do know the molecular formula,
        please consult "Molar Mass of a particle (M)"''')


        if method_m is not None:


            if method_m == 'n & M  (Number of moles & Molar mass)':
                n_m = st.number_input('Number of moles (mol)',
                              min_value=0.0, )
                M_m = st.number_input('Molar mass (g/mol)',
                              min_value=0.0, )
                if st.button('Calculate mass'):
                    if M_m == 0:
                        st.error('Mass cannot be calculated (Molar mass should be non-zero)')
                    else:
                        m = n_m * M_m
                        st.success(f"Mass = {m} g")


            elif method_m == 'Cm & Vs  (Mass concentration of a solution & Total volume of that solution)':
                Cm_m = st.number_input('Mass concentration (g/L)',
                               min_value=0.0, )
                Vs_m = st.number_input('Total volume of solution (L)',
                               min_value=0.0, )
                if st.button('Calculate mass'):
                    if Vs_m == 0:
                        st.error('Mass cannot be calculated (Volume should be non-zero)')
                    else:
                         m = Cm_m * Vs_m
                         st.success(f"Mass = {m} g")


            elif method_m == 'x & M  (Number of particles in the body & Molar mass)':
                x_m = st.number_input('Number of particles',
                              min_value=0.0, )
                M_m = st.number_input('Molar mass (g/mol)',
                              min_value=0.0, )
                if st.button('Calculate mass'):
                    m = x_m * M_m / 6.02e23
                    st.success(f"Mass = {m} g")


            elif method_m == 'ρ & V  (Volumic mass / Density & Volume of the body)':
                p_m = st.number_input('Volumic mass / Density (g/cm³)',
                              min_value=0.0, )
                V_m = st.number_input('Body volume (mL)',
                              min_value=0.0, )
                if st.button('Calculate mass'):
                    m = p_m * V_m
                    st.success(f"Mass = {m} g")


            elif method_m == 'CM, Vs & M  (Molar concentration & total volume of a solution, plus the molar mass of solute)':
                CM_m = st.number_input('Molar concentration (mol/L)',
                               min_value=0.0, )
                Vs_m = st.number_input('Total volume of solution (L)',
                               min_value=0.0, )
                M_m = st.number_input('Molar mass (g/mol)',
                              min_value=0.0, )
                if st.button('Calculate mass'):
                    m = CM_m * Vs_m * M_m
                    st.success(f"Mass = {m} g")


            elif method_m == 'IF GAS: V & M (Gas volume & Molar mass of gas)':
                V_m = st.number_input('Gas volume (L)',
                              min_value=0.0, )
                M_m = st.number_input('Molar mass (g/mol)',)
                if st.button('Calculate interval of mass'):
                    m1 = V_m * M_m / 24
                    m2 = V_m * M_m / 22.4
                    st.success(f"Mass between {m1} and {m2} g (depending on room conditions)")



    elif quantity == 'Volume of the body (V)':

        method_V = st.selectbox('Please select the data set that you have',
                            ('m & ρ (Body mass & Volumic mass / Density)',
                             'n, M & ρ (Number of moles in body, Molar mass & Volumic mass / Density)',
                             'x, M & ρ  (Number of particles in the body, Molar mass & Volumic mass / Density)',
                             'IF GAS: n (Number of moles)',
                             'IF GAS: m & M (Gas mass & Molar mass)',
                             'IF GAS: x (Number of particles in gas'),
                                index=None,
                                placeholder='Select the data set that you have',
                            )
        print(''' Choose the method based on the data you have
          If you don't know the molar mass but do know the molecular formula,
           please consult "Molar Mass of a particle (M)"''')


        if method_V is not None:


            if method_V == 'm & ρ (Body mass & Volumic mass / Density)':
                m_V = st.number_input('Mass (g)',
                              min_value=0.0, )
                ρ_V = st.number_input('Volumic mass / Density (g/cm³)',
                              min_value=0.0, )
                if st.button('Calculate Volume'):
                    if ρ_V == 0:
                        st.error('Volume cannot be calculated (Volumic mass / Density should be non-zero)')
                    else:
                        V = m_V / ρ_V
                        VL = V / 1000
                        st.success(f"Volume = {V} mL or {VL} L")


            elif method_V == 'n, M & ρ (Number of moles in body, Molar mass & Volumic mass / Density)':
                n_V = st.number_input('Number of moles (mol)',
                              min_value=0.0, )
                M_V = st.number_input('Molar mass (g/mol)',
                              min_value=0.0, )
                ρ_V = st.number_input('Volumic mass / Density (g/cm³)',
                              min_value=0.0, )
                if st.button('Calculate Volume'):
                    if ρ_V == 0:
                        st.error('Volume cannot be calculated (Volumic mass / Density should be non-zero)')
                    else:
                        V = n_V * M_V / ρ_V
                        VL = V / 1000
                        st.success(f"Volume = {V} mL or {VL} L")


            elif method_V == 'x, M & ρ  (Number of particles in the body, Molar mass & Volumic mass / Density)':
                x_V = st.number_input('Number of particles',
                              min_value=0.0, )
                M_V = st.number_input('Molar mass (g/mol)',
                              min_value=0.0, )
                ρ_V = st.number_input('Volumic mass / Density (g/cm³)',
                              min_value=0.0, )
                if st.button('Calculate Volume'):
                    if ρ_V == 0:
                        st.error('Volume cannot be calculated (Volumic mass / Density should be non-zero)')
                    else:
                        V = ( x_V * M_V ) / ( ρ_V * 6.02e23 )
                        VL = V / 1000
                        st.success(f"Volume = {V} mL or {VL} L")


            elif method_V == 'IF GAS: n (Number of moles)':
                n_V = st.number_input('Number of moles (mol)',
                              min_value=0.0, )
                if st.button('Calculate interval of Volume'):
                    V1 = 22.4 * n_V
                    V2 = 24 * n_V
                    st.success(f"Volume between {V1} and {V2} L (depending on room conditions)")


            elif method_V == 'IF GAS: m & M (Gas mass & Molar mass)':
                m_V = st.number_input('Gas mass (g)',
                                  min_value=0.0, )
                M_V = st.number_input('Molar mass (g/mol)',
                              min_value=0.0, )
                if st.button('Calculate interval of Volume'):
                    if M_V == 0:
                        st.error('Volume cannot be calculated (Molar mass should be non-zero)')
                    else:
                        V1 = 22.4 * m_V / M_V
                        V2 = 24 * m_V / M_V
                        st.success(f"Volume between {V1} and {V2} L (depending on room conditions)")


            elif method_V == 'IF GAS: x (Number of particles in gas':
                x_V = st.number_input('Number of particles',
                                  min_value=0.0, )
                if st.button('Calculate interval of Volume'):
                    V1 = 22.4 * x_V / 6.02e23
                    V2 = 24 * x_V / 6.02e23
                    st.success(f"Volume between {V1} and {V2} L (depending on room conditions)")



    elif quantity == 'Volume of a solution (Vs)':

        method_Vs = st.selectbox('Please select the data set that you have',
                            ('n & CM  (Number of moles in solute & Molar concentration of solution)',
        'm & Cm  (Mass of solute & Mass concentration of solution)',
        'n, M & Cm (Number of moles in solute, Molar mass & Mass concentration of solution)',
        'm, M & CM (Mass of solute, Molar mass & Molar concentration of solution)',
        'x & CM (Number of particles in solute & Molar concentration of solution)',
        'x, M & Cm (Number of particles in solute, Molar mass & Mass concentration of solution)'),
                                 index=None,
                                 placeholder='Select the data set that you have',
                             )
        print(''' Choose the method based on the data you have
        If you don't know the molar mass but do know the molecular formula,
        please consult "Molar Mass of a particle (M)"''')


        if method_Vs is not None:


            if method_Vs == 'n & CM  (Number of moles in solute & Molar concentration of solution)':
                n_Vs = st.number_input('Number of moles (mol)',
                              min_value=0.0, )
                CM_Vs = st.number_input('Molar concentration (mol/L)',
                              min_value=0.0, )
                if st.button('Calculate Volume of solution'):
                    if CM_Vs == 0:
                        st.error('Volume cannot be calculated (Molar concentration should be non-zero)')
                    else:
                        Vs = n_Vs / CM_Vs
                        st.success(f"Volume = {Vs} L")


            elif method_Vs == 'm & Cm  (Mass of solute & Massic concentration of solution)':
                m_Vs = st.number_input('Mass (g)',
                               min_value=0.0, )
                Cm_Vs = st.number_input('Massic concentration (g/L)',
                                min_value=0.0, )
                if st.button('Calculate Volume of solution'):
                    if Cm_Vs == 0:
                        st.error('Volume cannot be calculated (Mass concentration should be non-zero)')
                    else:
                        Vs = m_Vs / Cm_Vs
                        st.success(f"Volume = {Vs} L")


            elif method_Vs == 'n, M & Cm (Number of moles in solute, Molar mass & Mass concentration of solution)':
                n_Vs = st.number_input('Number of moles (mol)',
                               min_value=0.0, )
                M_Vs = st.number_input('Molar mass (g/mol)',)
                Cm_Vs = st.number_input('Mass concentration (g/L)',
                                min_value=0.0, )
                if st.button('Calculate Volume of solution'):
                    if Cm_Vs == 0:
                        st.error('Volume cannot be calculated (Mass concentration should be non-zero)')
                    else:
                        Vs = ( n_Vs * M_Vs ) / Cm_Vs
                        st.success(f"Volume = {Vs} L")


            elif method_Vs == 'm, M & CM (Mass of solute, Molar mass & Molar concentration of solution)':
                m_Vs = st.number_input('Mass (g)',
                               min_value=0.0, )
                M_Vs = st.number_input('Molar mass (g/mol)',
                                       min_value=0.0, )
                CM_Vs = st.number_input('Molar concentration (mol/L)',
                                min_value=0.0, )
                if st.button('Calculate Volume of solution'):
                    if CM_Vs == 0 or M_Vs == 0:
                        st.error('Volume cannot be calculated (Molar mass & Molar concentration should be non-zero)')
                    else:
                        Vs = m_Vs / (CM_Vs * M_Vs )
                        st.success(f"Volume = {Vs} L")


            elif method_Vs == 'x & CM (Number of particles in solute & Molar concentration of solution)':
                x_Vs = st.number_input('Number of particles',
                               min_value=0.0, )
                CM_Vs = st.number_input('Molar concentration (mol/L)',
                                min_value=0.0, )
                if st.button('Calculate Volume of solution'):
                    if CM_Vs == 0:
                        st.error('Volume cannot be calculated (Molar concentration should be non-zero)')
                    else:
                        Vs = x_Vs / (CM_Vs * 6.02e23 )
                        st.success(f"Volume = {Vs} L")


            elif method_Vs == 'x, M & Cm (Number of particles in solute, Molar mass & Mass concentration of solution)':
                x_Vs = st.number_input('Number of particles',
                                       min_value=0.0, )
                M_Vs = st.number_input('Molar mass (g/mol)',
                                       min_value=0.0, )
                Cm_Vs = st.number_input('Mass concentration (g/L)',
                                       min_value=0.0, )
                if st.button('Calculate Volume of solution'):
                    if Cm_Vs == 0:
                        st.error('Volume cannot be calculated (Mass concentration should be non-zero)')
                    else:
                        Vs = ( x_Vs * M_Vs ) / (Cm_Vs * 6.02e23 )
                        st.success(f"Volume = {Vs} L")



    elif quantity == 'Mass concentration (Cm)':

        method_Cm = st.selectbox('Please select the data set that you have',
                                 ('m & Vs (Mass of solute & Volume of solution)',
                                  'CM & M  (Molar concentration of solution & Molar mass of solute)',
                                  'n, M & Vs (Number of moles in solute, Molar mass & Volume of solution)',
                                  'm, n & CM (Mass of solute, number of moles in solute & Molar concentration of solution)',
                                  'x, M & Vs (Number of particles in solute, Molar mass of solute & Volume of solution)'),
                                 index=None,
                                 placeholder='Select the data set that you have',
                                 )
        print(''' Choose the method based on the data you have
               If you don't know the molar mass but do know the molecular formula,
               please consult "Molar Mass of a particle (M)"''')


        if method_Cm is not None:


            if method_Cm == 'm & Vs (Mass of solute & Volume of solution)':
                m_Cm = st.number_input('Mass (g)',
                                       min_value=0.0, )
                Vs_Cm = st.number_input('Volume (L)',
                                        min_value=0.0, )
                if st.button('Calculate Massic concentration'):
                    if Vs_Cm == 0:
                        st.error('Concentration cannot be calculated (Volume should be non-zero)')
                    else:
                        Cm = m_Cm / Vs_Cm
                        st.success(f"Mass concentration = {Cm} g/L")


            elif method_Cm == 'CM & M  (Molar concentration of solution & Molar mass of solute)':
                CM_Cm = st.number_input('Molar concentration (mol/L)',
                                       min_value=0.0, )
                M_Cm = st.number_input('Molar mass (g/mol)',
                                        min_value=0.0, )
                if st.button('Calculate Massic concentration'):
                    Cm = CM_Cm * M_Cm
                    st.success(f"Mass concentration = {Cm} g/L")


            elif method_Cm == 'n, M & Vs (Number of moles in solute, Molar mass & Volume of solution)':
                n_Cm = st.number_input('Number of moles (mol)',
                                       min_value=0.0, )
                M_Cm = st.number_input('Molar mass (g/mol)',
                                        min_value=0.0, )
                Vs_Cm = st.number_input('Volume of solution (L)',
                                        min_value=0.0, )
                if st.button('Calculate Massic concentration'):
                    if Vs_Cm == 0:
                        st.error('Concentration cannot be calculated (Volume should be non-zero)')
                    else:
                        Cm = ( n_Cm * M_Cm ) / Vs_Cm
                        st.success(f"Mass concentration = {Cm} g/L")


            elif method_Cm == 'm, n & CM (Mass of solute, number of moles in solute & Molar concentration of solution)':
                n_Cm = st.number_input('Number of moles (mol)',
                                       min_value=0.0, )
                m_Cm = st.number_input('Mass (g)',
                                        min_value=0.0, )
                CM_Cm = st.number_input('Molar concentration (mol/L)',
                                        min_value=0.0, )
                if st.button('Calculate Massic concentration'):
                    if n_Cm == 0:
                        st.error('Concentration cannot be calculated (Moles should be non-zero)')
                    else:
                        Cm = ( m_Cm * CM_Cm ) / n_Cm
                        st.success(f"Mass concentration = {Cm} g/L")


            elif method_Cm == 'x, M & Vs (Number of particles in solute, Molar mass of solute & Volume of solution)':
                x_Cm = st.number_input('Number of particles',
                                       min_value=0.0, )
                M_Cm = st.number_input('Molar mass (g/mol)',
                                        min_value=0.0, )
                Vs_Cm = st.number_input('Volume of solution (L)',
                                        min_value=0.0, )
                if st.button('Calculate Massic concentration'):
                    if Vs_Cm == 0:
                        st.error('Concentration cannot be calculated (Volume should be non-zero)')
                    else:
                        Cm = ( x_Cm * M_Cm ) / ( Vs_Cm * 6.02e23 )
                        st.success(f"Mass concentration = {Cm} g/L")



    elif quantity == 'Molar concentration (CM)':

        method_CM = st.selectbox('Please select the data set that you have',
                                 ('n & Vs (Number of moles & Volume of solution)',
                                  'Cm & M  (Mass concentration of solution & Molar mass of solute)',
                                  'm, M & Vs (Mass of solute, Molar mass & Volume of solution)',
                                  'm, n & Cm (Mass of solute, number of moles in solute & Mass concentration of solution)'
                                  'x & Vs (Number of particles in solute & Volume of solution)'),
                                 index=None,
                                 placeholder='Select the data set that you have',
                                 )
        print(''' Choose the method based on the data you have
                       If you don't know the molar mass but do know the molecular formula,
                       please consult "Molar Mass of a particle (M)"''')

        if method_CM is not None:

            if method_CM == 'n & Vs (Number of moles & Volume of solution)':
                n_CM = st.number_input('Number of moles (mol)',
                                       min_value=0.0, )
                Vs_CM = st.number_input('Volume (L)',
                                        min_value=0.0, )
                if st.button('Calculate Molar concentration'):
                    if Vs_CM == 0:
                        st.error('Concentration cannot be calculated (Volume should be non-zero)')
                    else:
                        CM = n_CM / Vs_CM
                        st.success(f"Mass concentration = {CM} mol/L")


            elif method_CM == 'Cm & M  (Mass concentration of solution & Molar mass of solute)':
                Cm_CM = st.number_input('Mass concentration (g/L)',
                                       min_value=0.0, )
                M_CM = st.number_input('Molar mass (g/mol)',
                                        min_value=0.0, )
                if st.button('Calculate Molar concentration'):
                    if M_CM == 0:
                        st.error('Concentration cannot be calculated (Molar mass should be non-zero)')
                    else:
                        CM = Cm_CM / M_CM
                        st.success(f"Mass concentration = {CM} mol/L")

            elif method_CM == 'm, M & Vs (Mass of solute, Molar mass & Volume of solution)':
                m_CM = st.number_input('Mass (g)',
                                        min_value=0.0, )
                M_CM = st.number_input('Molar mass (g/mol)',
                                       min_value=0.0, )
                Vs_CM = st.number_input('Volume of solution (L)',
                                        min_value=0.0, )
                if st.button('Calculate Molar concentration'):
                    if M_CM == 0 or Vs_CM == 0:
                        st.error('Concentration cannot be calculated (Molar mass & volume should be non-zero)')
                    else:
                        CM = m_CM / ( M_CM * Vs_CM )
                        st.success(f"Mass concentration = {CM} mol/L")


            elif method_CM == 'm, n & Cm (Mass of solute, number of moles in solute & Mass concentration of solution)':
                m_CM = st.number_input('Mass (g)',
                                        min_value=0.0, )
                n_CM = st.number_input('Number of moles (mol)',
                                       min_value=0.0, )
                Cm_CM = st.number_input('Mass concentration (g/L)',
                                        min_value=0.0, )
                if st.button('Calculate Molar concentration'):
                    if m_CM == 0:
                        st.error('Concentration cannot be calculated (Mass should be non-zero)')
                    else:
                        CM = n_CM * Cm_CM / m_CM
                        st.success(f"Mass concentration = {CM} mol/L")


            elif method_CM == 'x & Vs (Number of particles in solute & Volume of solution)':
                x_CM = st.number_input('Number of particles',
                                        min_value=0.0, )
                Vs_CM = st.number_input('Volume of solution (L)',
                                       min_value=0.0, )
                if st.button('Calculate Molar concentration'):
                    if Vs_CM == 0:
                        st.error('Concentration cannot be calculated (Volume should be non-zero)')
                    else:
                        CM = x_CM / ( Vs_CM * 6.02e23 )
                        st.success(f"Mass concentration = {CM} mol/L")



    elif quantity == 'Volumic mass / Density (ρ)':

        method_p = st.selectbox('Please select the data set that you have',
                                 ('m & V (Body mass & Volume)',
                                  'n, M & V (Number of moles, Molar mass & Volume)',
                                  'x, M & V (Number of particles, Molar mass & Volume)',
                                  'IF GAS: M (Molar mass of gas)'),
                                 index=None,
                                 placeholder='Select the data set that you have',
                                 )
        print(''' Choose the method based on the data you have
                       If you don't know the molar mass but do know the molecular formula,
                       please consult "Molar Mass of a particle (M)"''')

        if method_p is not None:

            if method_p == 'm & V (Body mass & Volume)':
                m_p = st.number_input('Mass (g)',
                                       min_value=0.0, )
                V_p = st.number_input('Volume (L)',
                                        min_value=0.0, )
                if st.button('Calculate Volumic mass'):
                    if V_p == 0:
                        st.error('Volumic mass cannot be calculated (Volume should be non-zero)')
                    else:
                        p = m_p / ( V_p * 1000 )
                        st.success(f"Volumic mass = {p} g/cm³")


            elif method_p == 'n, M & V (Number of moles, Molar mass & Volume)':
                n_p = st.number_input('Number of moles (mol)',
                                      min_value=0.0, )
                M_p = st.number_input('Molar mass (g/mol)',
                                      min_value=0.0, )
                V_p = st.number_input('Volume (L)',
                                      min_value=0.0, )
                if st.button('Calculate Volumic mass'):
                    if V_p == 0:
                        st.error('Volumic mass cannot be calculated (Volume should be non-zero)')
                    else:
                        p = ( n_p * M_p ) / (V_p * 1000)
                        st.success(f"Volumic mass = {p} g/cm³")


            elif method_p == 'x, M & V (Number of particles, Molar mass & Volume)':
                x_p = st.number_input('Number of particles',
                                      min_value=0.0, )
                M_p = st.number_input('Molar mass (g/mol)',
                                      min_value=0.0, )
                V_p = st.number_input('Volume (L)',
                                      min_value=0.0, )
                if st.button('Calculate Volumic mass'):
                    if V_p == 0:
                        st.error('Volumic mass cannot be calculated (Volume should be non-zero)')
                    else:
                        p = (x_p * M_p) / (V_p * 1000 * 6.02e23 )
                        st.success(f"Volumic mass = {p} g/cm³")


            elif method_p == 'IF GAS: M (Molar mass of gas)':
                M_p = st.number_input('Molar mass (g/mol)',
                                      min_value=0.0, )
                if st.button('Calculate Volumic mass'):
                    p1 = M_p / 24
                    p2 = M_p / 22.4
                    st.success(f"Volumic mass between {p1} and {p2} g/cm³ (depending on room conditions)")



    elif quantity == 'Number of particles (x)':

        method_x = st.selectbox('Please select the data set that you have',
                                 ('n (Number of moles)',
                                  'm & M (Body mass & Molar mass)',
                                  'ρ, M & V (Volumic mass / Density, Molar mass & Volume)',
                                  'CM & Vs (Molar concentration of solution & Volume of solution)',
                                  'Cm, M & Vs (Mass concentration of solution, Molar mass of solute & Volume of solution)',
                                  'IF GAS: V (Volume of gas)'),
                                 index=None,
                                 placeholder='Select the data set that you have',
                                 )
        print(''' Choose the method based on the data you have
                       If you don't know the molar mass but do know the molecular formula,
                       please consult "Molar Mass of a particle (M)"''')

        if method_x is not None:

            if method_x == 'n (Number of moles)':
                n_x = st.number_input('Number of moles (mol)',
                                       min_value=0.0, )
                if st.button('Calculate number of particles'):
                    x = n_x * 6.02e23
                    st.success(f"Number of particles = {x}")


            elif method_x == 'm & M (Body mass & Molar mass)':
                m_x = st.number_input('Mass (g)',
                                      min_value=0.0, )
                M_x = st.number_input('Molar mass (g/mol)',
                                      min_value=0.0, )
                if st.button('Calculate number of particles'):
                    if M_x == 0:
                        st.error('Number of particles cannot be calculated (Molar mass should be non-zero)')
                    else:
                        x = ( m_x * 6.02e23 ) / M_x
                        st.success(f"Number of particles = {x}")


            elif method_x == 'ρ, M & V (Volumic mass / Density, Molar mass & Volume)':
                p_x = st.number_input('Volumic mass / Density (g/cm³)',
                                      min_value=0.0, )
                M_x = st.number_input('Molar mass (g/mol)',
                                      min_value=0.0, )
                V_x = st.number_input('Volume (L)',
                                      min_value=0.0, )
                if st.button('Calculate number of particles'):
                    if M_x == 0:
                        st.error('Number of particles cannot be calculated (Molar mass should be non-zero)')
                    else:
                        x = ( p_x * V_x * 6.02e23 ) / M_x
                        st.success(f"Number of particles = {x}")


            elif method_x == 'CM & Vs (Molar concentration of solution & Volume of solution)':
                CM_x = st.number_input('Molar concentration (mol/L)',
                                      min_value=0.0, )
                Vs_x = st.number_input('Volume (L)',
                                      min_value=0.0, )
                if st.button('Calculate number of particles'):
                    x = CM_x * Vs_x * 6.02e23
                    st.success(f"Number of particles = {x}")


            elif method_x == 'Cm, M & Vs (Mass concentration of solution, Molar mass of solute & Volume of solution)':
                Cm_x = st.number_input('Mass concentration (g/L)',
                                      min_value=0.0, )
                M_x = st.number_input('Molar mass (g/mol)',
                                      min_value=0.0, )
                Vs_x = st.number_input('Volume (L)',
                                      min_value=0.0, )
                if st.button('Calculate number of particles'):
                    if M_x == 0:
                        st.error('Number of particles cannot be calculated (Molar mass should be non-zero)')
                    else:
                        x = (Cm_x * Vs_x * 6.02e23) / M_x
                        st.success(f"Number of particles = {x}")


            elif method_x == 'IF GAS: V (Volume of gas)':
                V_x = st.number_input('Volume (L)',
                                       min_value=0.0, )
                if st.button('Calculate number of particles'):
                    x1 = ( V_x * 6.02e23 ) / 24
                    x2 = ( V_x * 6.02e23 ) / 22.4
                    st.success(f"Number of particles between {x1} and {x2} L (depending on room conditions)")



    elif quantity == 'Molar Mass of a particle (M)':

        method_M = st.selectbox('Please select the data set that you have',
                                 ("PARTICLE'S CONSTITUTING ELEMENTS",
                                  'n & m (Number of moles & Body mass)',
                                  'ρ, V & n (Volumic mass / Density, Volume & Number of moles)',
                                  'Cm, Vs & n (Mass concentration of solution, Volume of solution & Number of moles in solute)',
                                  'm, CM & Vs (Mass of solute, Molar concentration & Volume of solution)',
                                  'Cm & CM(Mass concentration of solution & Molar concentration of solution)',
                                  'm & x (Mass of body & Number of particles)',
                                  'V, ρ & x (Volume, Volumic mass / Density & Number of particles)',
                                  'Cm, Vs & x (Mass concentration of solution, Volume of solution & Number of particles in solute)',
                                  'IF GAS: m & V (Mass & Volume of gas)'),
                                 index=None,
                                 placeholder='Select the data set that you have',
                                 )
        print(''' Choose the method based on the data you have ''')

        if method_M is not None:

            if method_M == 'n & m (Number of moles & Body mass)':
                n_M = st.number_input('Number of moles (mol)',
                                       min_value=0.0, )
                m_M = st.number_input('Mass (g)',
                                      min_value=0.0, )
                if st.button('Calculate Molar mass'):
                    if n_M == 0:
                        st.error('Molar mass cannot be calculated (Number of moles should be non-zero)')
                    else:
                        M = m_M / n_M
                        st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'ρ, V & n (Volumic mass / Density, Volume & Number of moles)':
                p_M = st.number_input('Volumic mass / Density (g/cm³)',
                                       min_value=0.0, )
                V_M = st.number_input('Mass (g)',
                                      min_value=0.0, )
                n_M = st.number_input('Number of moles',
                                      min_value=0.0, )
                if n_M == 0:
                    st.error('Molar mass cannot be calculated (Number of moles should be non-zero)')
                else:
                    M = ( p_M * V_M ) / n_M
                    st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'm, CM & Vs (Mass of solute, Molar concentration & Volume of solution)':
                m_M = st.number_input('Mass (g)',
                                       min_value=0.0, )
                CM_M = st.number_input('Molar concentration (mol/L)',
                                       min_value=0.0, )
                Vs_M = st.number_input('Volume (L)',
                                      min_value=0.0, )
                if CM_M == 0 or Vs_M == 0:
                    st.error('Molar mass cannot be calculated (Molar concentration & Volume should be non-zero)')
                else:
                    M = m_M / ( CM_M * Vs_M )
                    st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'Cm, Vs & n (Mass concentration of solution, Volume of solution & Number of moles in solute)':
                Cm_M = st.number_input('Mass concentration (g/L)',
                                       min_value=0.0, )
                Vs_M = st.number_input('Volume (L)',
                                      min_value=0.0, )
                n_M = st.number_input('Number of moles',
                                      min_value=0.0, )
                if n_M == 0:
                    st.error('Molar mass cannot be calculated (Number of moles should be non-zero)')
                else:
                    M = ( Cm_M * Vs_M ) / n_M
                    st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'Cm & CM(Mass concentration of solution & Molar concentration of solution)':
                Cm_M = st.number_input('Mass concentration (g/L)',
                                       min_value=0.0, )
                CM_M = st.number_input('Molar concentration (mol/L)',
                                       min_value=0.0, )
                if CM_M == 0:
                    st.error('Molar mass cannot be calculated (Molar concentration should be non-zero)')
                else:
                    M = Cm_M / CM_M
                    st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'm & x (Mass of body & Number of particles)':
                m_M = st.number_input('Mass (g)',
                                       min_value=0.0, )
                x_M = st.number_input('Number of particles',
                                       min_value=0.0, )
                if x_M == 0:
                    st.error('Molar mass cannot be calculated (Number of particles should be non-zero)')
                else:
                    M = ( m_M * 6.02e23 ) / x_M
                    st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'V, ρ & x (Volume, Volumic mass / Density & Number of particles)':
                V_M = st.number_input('Volume (L)',
                                       min_value=0.0, )
                p_M = st.number_input('Volumic mass / Density (g/cm³)',
                                      min_value=0.0, )
                x_M = st.number_input('Number of particles',
                                       min_value=0.0, )
                if x_M == 0:
                    st.error('Molar mass cannot be calculated (Number of particles should be non-zero)')
                else:
                    M = ( V_M * p_M * 6.02e23 ) / x_M
                    st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'Cm, Vs & x (Mass concentration of solution, Volume of solution & Number of particles in solute)':
                Cm_M = st.number_input('Mass concentration (g/L)',
                                      min_value=0.0, )
                Vs_M = st.number_input('Volume (L)',
                                      min_value=0.0, )
                x_M = st.number_input('Number of particles',
                                      min_value=0.0, )
                if x_M == 0:
                    st.error('Molar mass cannot be calculated (Number of particles should be non-zero)')
                else:
                    M = (Cm_M * Vs_M * 6.02e23) / x_M
                    st.success(f"Molar mass = {M} g/mol")


            elif method_M == 'IF GAS: m & V (Mass & Volume of gas)':
                m_M = st.number_input('Mass (g)',
                                      min_value=0.0, )
                V_M = st.number_input('Volume (L)',
                                      min_value=0.0, )
                if V_M == 0:
                    st.error('Molar mass cannot be calculated (Volume should be non-zero)')
                else:
                    M1 = ( m_M * 22.4 ) / V_M
                    M2 = ( m_M * 24 ) / V_M
                    st.success(f"Molar mass between {M1} and {M2} g/mol (depending on room conditions)")


            elif method_M == "PARTICLE'S CONSTITUTING ELEMENTS":
                elements = {
                    "Hydrogen (H)": 1.008,
                    "Helium (He)": 4.003,
                    "Lithium (Li)": 6.94,
                    "Beryllium (Be)": 9.012,
                    "Boron (B)": 10.81,
                    "Carbon (C)": 12.011,
                    "Nitrogen (N)": 14.007,
                    "Oxygen (O)": 15.999,
                    "Fluorine (F)": 18.998,
                    "Neon (Ne)": 20.180,
                    "Sodium (Na)": 22.990,
                    "Magnesium (Mg)": 24.305,
                    "Aluminium (Al)": 26.982,
                    "Silicon (Si)": 28.085,
                    "Phosphorus (P)": 30.974,
                    "Sulfur (S)": 32.06,
                    "Chlorine (Cl)": 35.45,
                    "Potassium (K)": 39.098,
                    "Calcium (Ca)": 40.078,
                    "Iron (Fe)": 55.845,
                    "Copper (Cu)": 63.546,
                    "Zinc (Zn)": 65.38,
                    "Bromine (Br)": 79.904,
                    "Silver (Ag)": 107.868,
                    "Iodine (I)": 126.904,
                    "Barium (Ba)": 137.327,
                    "Gold (Au)": 196.967,
                    "Mercury (Hg)": 200.592
                }
                selected_elements = st.multiselect(
                    "Step 1: Choose the elements in your molecule:",
                    options=list(elements.keys())
                )
                if selected_elements:

                    st.write("Step 2: Specify the number of atoms")

                    atom_counts = {}

                    for element in selected_elements:

                        atom_counts[element] = st.number_input(
                            f"Number of {element} atoms:",
                            min_value=1,
                            value=1,
                            step=1,
                            key=element
                        )
                if st.button("Calculate molar mass"):

                    molar_mass = 0
                    formula = ""

                    for element in selected_elements:

                        atomic_mass = elements[element]
                        number_of_atoms = atom_counts[element]

                        molar_mass += atomic_mass * number_of_atoms
                    st.success(f'Molar mass = {molar_mass:.3f} g/mol')
                else:
                    st.info("Please select at least one element to proceed.")