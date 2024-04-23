import React from "react";
import styled from "styled-components";

import Item from "./Item";

const MenuContainer = styled.div`
    padding: 4px 16px;
    font-size: var(--font-small);
    font-family: outfit;
`

const JobsContainer = styled.div`
    display: grid;
    gap: 4px;
    grid-template-columns: 1fr 1fr;
    margin-top: 4px;
`

interface DashboardVerticalMenuProps {
    jobs: Array<string>
}

const DashboardVerticalMenu: React.FC<DashboardVerticalMenuProps> = ({ jobs }) => {
    return (
        <MenuContainer>
            Selecionar vagas
            <JobsContainer>
                {jobs.map((job, index) => {
                    return <Item key={job+index} name={job}/>
                })}

            </JobsContainer>
        </MenuContainer>
    )
}

export default DashboardVerticalMenu