import React from "react";
import styled from "styled-components";

import Layout from "../../layout";
import DashboardVerticalMenu from "../../components/DashboardVerticalMenu";
import SearchMenu from "../../components/SearchMenu";

const jobs: Array<string> = ["Django", "React", "Nest.js", "FastAPI", "React Native"];

const DashboardContainer = styled.div`
    display: grid;
    grid-template-columns: 0fr 1fr;
`
const AppContent = styled.div`
    height: 100vh;
`

const Dashboard: React.FC = () => {

    return (
        <Layout>
            <DashboardContainer>
                <DashboardVerticalMenu jobs={jobs}/>
                <AppContent>
                    <SearchMenu />
                    
                    <p>Dashboard page</p>
                </AppContent>
            </DashboardContainer>
        </Layout>
    )
}

export default Dashboard;