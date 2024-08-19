import React, {useState} from "react";
import styled from "styled-components";

import LupeIcon from "../../assets/lupe.svg";

const SearchContainer = styled.div`
`
const SearchRow = styled.div`
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 24px;
`
const AppliedFilters = styled.div`
    display: flex;
`

const FieldSelector = styled.select`
    border: 1px solid var(--black);
    border-radius: 8px;
    background-color: var(--white);
    padding: 4px 8px;
    font-family: 'outfit';
`

const SearchBarContainer = styled.div`
    display: flex;
    max-width: 600px;
`
const Input = styled.input`
    padding: 0px;
    margin: 0px;
    border-collapse: collapse;
    width: 100%;
    border-radius 8px;
    padding-left: 6px;
`

const IconContainer = styled.div`
    display: flex;
    padding: 0px 4px;
    border-left: 1px solid var(--black);
    border-top: 1px solid var(--black);
    border-bottom: 1px solid var(--black);
    border-right: none;
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
    
`
const SearchBar: React.FC = () => {
    return (
        <SearchBarContainer>
            <IconContainer>
                <img style={{width: 18, height: 18, alignSelf: 'center'}} src={LupeIcon} alt="lupe icon" />
            </IconContainer>
            <Input placeholder="pesquisar..."/>
        </SearchBarContainer>
    )
}

const options: Array<string> = ["Cargo", "Modalidade", "Local", "Salário", "Experiência", "Requisitos técnicos"];

const SearchMenu: React.FC = () => {

    return (
        <SearchContainer>
            <SearchRow>
                <FieldSelector>
                    <option>Selecionar</option>
                    {options.map(option => (<option key={option}>{option}</option>))}
                </FieldSelector>

                <SearchBar />
            </SearchRow>

            <AppliedFilters>

            </AppliedFilters>

        </SearchContainer>
    );
}

export default SearchMenu;