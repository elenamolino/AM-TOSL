# TOSL agreement template

Please use the following prefixes by default:

```
@prefix : <http://example.com/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix tosl: <https://w3id.org/tosl/> .
@base <http://example.com> .
```

For each ODRL and TOSL namespace property, it is mandatory to ensure accurate and consistent usage by thoroughly studying their ontologies.

### Guidelines for Using the ODRL Agreement Class:
Agreement - a subclass of Policy that supports granting of Rules from assigner to assignee Parties.

- An Agreement **MUST** have at least one permission, prohibition, or obligation property values of type the `Permission`, `Prohibition`, and `Obligation`.
- An Agreement **MAY** have none, one or many methods of dispute resolution.
- An Agreement **MAY** have none, one or many limitations of liability or liabilities.
- An Agreement **MAY** have none, one, or many `profile` property values of type `IRI` to denote the ODRL Profile(s) that this Policy adheres to.
- An Agreement **MUST** specify one assigner, a `Provider` type (`:OpenAI a tosl:Provider`). This is the entity granting permissions or constraints, often the owner of the asset.

Example Case: For each ODRL Agreement you create in your TTL file, it is mandatory to include metadata using Dublin Core terms. Use the following template as a guide and ensure that your ODRL Policy includes the necessary metadata in accordance with the agreement.

```ttl
@prefix : <http://example.com/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix tosl: <https://w3id.org/tosl/> .
@base <http://example.com> .

:agreement01 a odrl:Agreement, odrl:Asset ;
    odrl:profile <https://w3id.org/tosl/> ;
    dcterms:source <https://openai.com/policies/eu-terms-of-use/> ;
    dcterms:title "The OpenAI Europe Terms of Use 2024"^^xsd:string ;
    dcterms:description "These Terms of Use govern the use of OpenAI's services, including ChatGPT and DALL·E."^^xsd:string;
    dcterms:creator "OpenAI"^^xsd:string ;
    dcterms:rightsHolder :OpenAI ;
    dcterms:issued "2024-12-11"^^xsd:date ;
    dcterms:requires 
        <https://openai.com/policies/usage-policies/>,
        <https://openai.com/policies/service-terms/>,
        <https://openai.com/policies/sharing-publication-policy/>,
        <https://openai.com/policies/service-credit-terms/>,
        <https://openai.com/brand/> ;
    odrl:permission :permission01, :permission02, :permission03, :permission04, :permission05 ;
    odrl:obligation :obligation01, :obligation02 ;
    odrl:prohibition :prohibition01, :prohibition02, :prohibition03 ;
    tosl:limitationOfLiability :liability04 ;
    tosl:onDispute :litigation01, :litigation02, :litigation03 ;
    tosl:liability :liability05 ;
    odrl:assigner :OpenAI .
```

### Guidelines for Using the ODRL Permission Class:
Permission - a Permission allows an action, with all refinements satisfied, to be exercised on an Asset if
all constraints are satisfied and if all duties are fulfilled.

- A **Permission MUST** have one `description` representing the agreement disposition.
- A **Permission MUST** have one `assignee` property value that is the recipient of the Rule.
- A **Permission MUST** have an `action` property value of type `Action`. It is mandatory that this action is an instance of **TOSL** or **ODRL**.
- A **Permission MUST** have one `target` property value of type `Asset`. Use the "Guidelines for Using the ODRL 'Asset' Class" for creating the `Asset` type for the `target` property.
- A **Permission MAY** have none, one or many `constraint` property values of type `Constraint` / `LogicalConstraint`.
- A **Permission MAY** have none, one or many limitations of liability or liabilities.
- A **Permission MAY** have none, one, or more `odrl:duty` property values of type `Duty`. The `duty` property asserts a **pre-condition**.
- A **Permission MAY** have none, one, or more `tosl:trigger` property values of type `Duty`. The `duty` property asserts a **post-condition**.

Use the following template as a guide and ensure that your permission is consistent with these
guidelines.

```ttl
@prefix : <http://example.com/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix tosl: <https://w3id.org/tosl/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:paidFeatures a tosl:Service ;
    dcterms:description "Premium features available only to paying subscribers." .

:OpenAI a tosl:Provider ;
    dcterms:description "OpenAI is an AI research and deployment company committed to ensuring that artificial general intelligence (AGI) benefits all of humanity."^^xsd:string ;
    foaf:name "Open AI" ;
    foaf:homepage <https://openai.com/> ;
    odrl:assignerOf :services .

:permission14 a odrl:Permission ;
    dcterms:description "We may change our prices from time to time. If we increase our subscription prices, we will give you at least 30 days’ notice and any price increase will take effect on your next renewal so that you can cancel if you do not agree to the price increase." ;
    odrl:action odrl:modify ;
    odrl:target :paidFeatures ;
    odrl:assignee :OpenAI ;
    odrl:constraint [
        a odrl:Constraint ;
        dcterms:description "At least 30 days’ notice must be provided before a price increase takes effect." ;
        odrl:leftOperand odrl:delayPeriod ;
        odrl:operator odrl:gteq ;
        odrl:rightOperand "P30D"^^xsd:duration
    ] ;
    odrl:duty [
        a odrl:Duty ;
        odrl:action odrl:inform ;
        odrl:target :paidFeatures ;
        odrl:assignee :OpenAI ;
        odrl:informedParty :customer
    ] .
```

### Guidelines for Using the ODRL Prohibition Class:
Prohibition - A Prohibition disallows an action, with all refinements satisfied, to be exercised on an
Asset if all constraints are satisfied. If the Prohibition has been infringed by the action being exercised,
then all the remedies MUST be fulfilled to set the state of the Prohibition to not infringed.

- A **Prohibition MUST** have one `description` representing the agreement disposition.
- A **Prohibition MUST** have one `assignee` property value that is the recipient of the Rule.
- A **Prohibition MUST** have an `action` property value of type `Action`. It is mandatory that this action is an instance of **TOSL** or **ODRL**.
- A **Prohibition MUST** have one `target` property value of type `Asset`. Use the *Guidelines for Using the ODRL 'Asset' Class* for creating the `Asset` type for the `target` property.
- A **Prohibition MAY** have none, one or many `constraint` property values of type `Constraint` / `LogicalConstraint`.
- A **Prohibition MAY** have none, one or many limitations of liability or liabilities.
- A **Prohibition MAY** have none, one, or more `odrl:remedy` property values of type `Duty`. The `remedy` property asserts an agreed obligation that **MUST** be fulfilled in the case that the Prohibition has been infringed.

Use the following template as a guide and ensure that your prohibition is consistent with these
guidelines.

```ttl
@prefix : <http://example.com/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix tosl: <https://w3id.org/tosl/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:prohibition03 a odrl:Prohibition ;
    dcterms:description "You must comply with all applicable trade laws, including sanctions and export control laws. Our Services may not be used in or for the benefit of, or exported or re-exported to: (a) any U.S. embargoed country or territory, or (b) any individual or entity with whom dealings are prohibited or restricted under applicable trade laws."^^xsd:string ;
    odrl:action odrl:use ;
    odrl:target :services ;
    odrl:assignee :customer ;
    odrl:constraint [
        a odrl:LogicalConstraint ;
        odrl:or (
            [
                a odrl:Constraint ;
                odrl:leftOperand odrl:spatial ;
                odrl:operator odrl:isAnyOf ;
                odrl:rightOperand ( "CU" "IR" "KP" "SY" "RU" )
            ]
            [
                a odrl:Constraint ;
                odrl:leftOperand tosl:compliance ;
                odrl:operator odrl:neq ;
                odrl:rightOperand :tradeLaw
            ]
        )
    ] .
```

### Guidelines for Using the ODRL Duty Class:
Duty - A Duty is an obligation to perform an action. It is fulfilled when all its constraints are met, and the action is executed. If the action is not executed, any defined consequences must also be fulfilled.

- A Duty **MUST** have one description representing the agreement disposition.
- A Duty **MUST** have one assignee property value that is the recipient of the Rule.
- A Duty **MUST** have an action property value of type *Action*. It is mandatory that this action is an instance of **TOSL** or **ODRL**.
- A Duty **MUST** have one target property value of type *Asset*. Use *Guidelines for Using the ODRL 'Asset' Class* for creating Asset Type for the target property.
- A Duty **MAY** have none, one or many constraint property values of type *Constraint/LogicalConstraint*.
- A Duty **MAY** have none, one or many limitations of liability or liabilities.
- A Duty **MAY** have none, one, or more `odrl:consequence` property values of type *Duty*. The `duty` property is used to express the repercussions of not fulfilling an agreed Policy obligation or duty for a Permission.

Use the following template as a guide and ensure that your duty is consistent with these
guidelines.

```ttl
:obligation01 a odrl:Duty ;
    dcterms:description "You form a contract with us when you confirm that you accept these Terms or when you otherwise use the Services." ;
    odrl:action tosl:consent ;
    odrl:constraint [
        a odrl:Constraint ;
        odrl:leftOperand tosl:consentType ;
        odrl:operator odrl:eq ;
        odrl:rightOperand tosl:implicitConsent
    ] ;
    odrl:target :agreement01 ;
    odrl:assignee :customer .
```

### Guidelines for Using the ODRL Action Class:
Action - An Action class indicates an operation that can be exercised on an Asset. An Action is associated with the Asset via the action property in a Rule.

The available instances of actions are predefined and must be used as provided. These actions come from both the **ODRL** and **TOSL** vocabularies:

**ODRL actions:**  
`odrl:acceptTracking`, `odrl:aggregate`, `odrl:anonymize`, `odrl:annotate`, `odrl:archive`, `odrl:attribute`, `odrl:compensate`, `odrl:concurrentUse`, `odrl:delete`, `odrl:derive`, `odrl:digitize`, `odrl:display`, `odrl:distribute`, `odrl:ensureExclusivity`, `odrl:execute`, `odrl:extract`, `odrl:give`, `odrl:grantUse`, `odrl:include`, `odrl:index`, `odrl:inform`, `odrl:install`, `odrl:modify`, `odrl:move`, `odrl:nextPolicy`, `odrl:obtainConsent`, `odrl:play`, `odrl:present`, `odrl:print`, `odrl:read`, `odrl:reproduce`, `odrl:reviewPolicy`, `odrl:sell`, `odrl:stream`, `odrl:synchronize`, `odrl:textToSpeech`, `odrl:transfer`, `odrl:transform`, `odrl:translate`, `odrl:uninstall`, `odrl:use`, `odrl:watermark`

**TOSL actions:**  
`tosl:allowDownload`, `tosl:appeal`, `tosl:assign`, `tosl:claim`, `tosl:consent`, `tosl:develop`, `tosl:evaluate`, `tosl:integrate`, `tosl:procedure`, `tosl:publish`, `tosl:remove`, `tosl:terminate`, `tosl:test`

### Guidelines for Using the ODRL Party Class:
Party - A Party is an entity (such as a person, organization, or agent) that must adopt a functional role in a Rule, such as tosl:Provider, tosl:Customer, or tosl:BusinessCustomer.

### Guidelines for Using the ODRL Asset Class:
Asset - An Asset is a resource or group of resources that are the subject of a Rule, such as data, media, services, or physical items. It is referenced by Permissions, Prohibitions and/or Duties, and must be of type odrl:Asset, tosl:Service, or tosl:UserContent.

### Guidelines for Using the ODRL Constraint Class:
Constraints - Constraints can be represented as a Constraint class or Logical Constraint class. A Logical Constraint will refer to existing Constraints as its operands. When multiple Constraints apply to the
same Rule, Action, Party/Asset Collection, then they are interpreted as conjunction, and all MUST be satisfied.

A **Logical Constraint** defines a logical relationship between multiple `Constraint` instances.  
It **MUST** include one operand sub-property (`odrl:or`, `odrl:xone`, `odrl:and`, or `odrl:andSequence`) indicating how the constraints are evaluated.

- A `Constraint` **MUST** have one `leftOperand` property whose value is of type `LeftOperand`.  
  This value should be selected from a predefined set of terms, including:  
  `odrl:absolutePosition`, `odrl:absoluteSpatialPosition`, `odrl:absoluteTemporalPosition`, `odrl:absoluteSize`, `odrl:count`, `odrl:dateTime`, `odrl:delayPeriod`, `odrl:deliveryChannel`, `odrl:elapsedTime`, `odrl:event`, `odrl:fileFormat`, `odrl:industry`, `odrl:language`, `odrl:media`, `odrl:meteredTime`, `odrl:payAmount`, `odrl:percentage`, `odrl:product`, `odrl:purpose`, `odrl:recipient`, `odrl:relativePosition`, `odrl:relativeSpatialPosition`, `odrl:relativeTemporalPosition`, `odrl:relativeSize`, `odrl:resolution`, `odrl:spatial`, `odrl:spatialCoordinates`, `odrl:systemDevice`, `odrl:timeInterval`, `odrl:unitOfCount`, `odrl:version`, `odrl:virtualLocation`, `tosl:justification`, `tosl:totalAmount`, `tosl:inactivityPeriod`, `tosl:consumerResidentCountry`, `tosl:consentType`, `tosl:compliance`, `tosl:licensingType`, `tosl:effect`, and `foaf:age`.  
  Alternatively, the value may be a custom IRI, as long as it is explicitly declared as an instance of `odrl:LeftOperand`.

- A `Constraint` **MUST** have one `operator` property whose value is of type `Operator`.  
  The allowed operator values are:  
  `odrl:eq`, `odrl:gt`, `odrl:gteq`, `odrl:lt`, `odrl:lteq`, `odrl:neq`, `odrl:isA`, `odrl:hasPart`, `odrl:isPartOf`, `odrl:isAllOf`, `odrl:isAnyOf`, and `odrl:isNoneOf`.

- A `Constraint` **MUST** have one `rightOperand` property, which provides the value to be evaluated against the condition defined by the `leftOperand` and `operator`.

- A `Constraint` **MAY** have none or one `unit` property value (of type IRI [rfc3987]) to set the unit used for the value of the `rightOperand`/Reference.


### Guidelines for Using the TOSL Dispute Resolution Class:

Dispute Resolution – Used to specify the mechanisms for resolving disputes among the parties involved in the agreement, such as arbitration or litigation. It is necessary to establish the location where disputes will be resolved and the specific legal framework that will apply.

- A Dispute Resolution **MAY** include `Litigation` or `Arbitration`.
- If `Litigation` is used, it **MAY** require `Arbitration` to be attempted first.
- A Dispute Resolution **MUST** include one `description` property of type `xsd:string`, providing a natural-language explanation of the term.
- A Dispute Resolution **MUST** have one `targetParty` property of type `Party`, identifying the party responsible for or affected by the process. This value should be either a `Customer` or a `BusinessCustomer`.
- A Dispute Resolution **MUST** have one `takePlaceIn` property of type `Jurisdiction`, specifying the court or legal venue where the resolution will occur.
- A Dispute Resolution **MUST** have one `governedBy` property of type `Law`, indicating the applicable legal framework.
- A Dispute Resolution **MUST** have none, one, or more `Constraint` instances representing specific conditions under which litigation may occur.

Example:
```ttl
:customer a tosl:Customer ;
    dcterms:description "This party represents the consumer in the context of the OpenAI services Terms of Use" .

:litigation02 a tosl:Litigation ;
    dcterms:description "If you reside in the EEA, you can also raise the dispute with an alternative dispute resolution body via the European Commission’s Online Dispute Resolution (ODR) Platform" ;
    tosl:targetParty :customer ;
    tosl:takesPlaceIn tosl:consumerPlaceCourts ;
    tosl:governedBy tosl:consumerPlaceLaw ;
    tosl:condition [
        a odrl:LogicalConstraint ;
        odrl:and (
            [
                a odrl:Constraint ;
                odrl:leftOperand tosl:consumerResidentCountry ;
                odrl:operator odrl:isAnyOf ;
                odrl:rightOperand (
                    "AT" "BE" "BG" "HR" "CY" "CZ" "DK" "EE" "FI" "FR" "DE" "GR" "HU" "IS" "IE" "IT" "LV" "LI" "LT" "LU" "MT" "NL" "NO" "PL" "PT" "RO" "SK" "SI" "ES" "SE" "CH"
                )
            ]
            [
                a odrl:Constraint ;
                odrl:leftOperand odrl:deliveryChannel ;
                odrl:operator odrl:eq ;
                odrl:rightOperand <https://ec.europa.eu/consumers/odr>
            ]
        )
    ] .

tosl:consumerPlaceCourts a tosl:Jurisdiction .
tosl:consumerPlaceLaw a tosl:Law .
```

### Guidelines for Using the TOSL Liability Class:
Liability - A Liability mechanism is used to define the extent to which a party is responsible for damages, losses, or obligations within an agreement. It can be used to establish either full liability or a limitation of liability under certain conditions.

- A `Liability` **MUST** include one `description` property of type `xsd:string`, providing a natural-language explanation of the liability terms.

- A `Liability` **MUST** have one `liableParty` property of type `Party`, identifying the party who bears the responsibility.  
  Valid values include: `tosl:Provider`, `tosl:Customer`, or `tosl:BusinessCustomer`.

- A `Liability` **MUST** have one `targetParty` property of type `Party`, identifying the party who is affected by or protected under the liability clause.  
  Accepted values are the same as for `liableParty`.

- A `Liability` **MUST** include one `rdf:value` property, specifying the type or scope of liability.  
  This value must be selected from a controlled set of terms defined in the TOSL vocabulary, such as:  
  `tosl:anyLiability`, `tosl:physicalInjuries`, `tosl:harmCausedByMalware`, `tosl:discontinuity`, `tosl:anyIndirectDamage`,  
  `tosl:directDamage`, `tosl:anyLoss`, `tosl:thirdparty`, `tosl:serviceContent`, `tosl:breachOfContract`, or `tosl:legalCompliance`.

- A `Liability` **MAY** include a `limitation` property. If present, the value **MUST** conform to either a `Constraint` or a `LogicalConstraint` structure.  
  This allows the liability to be conditional, depending on context or pre-defined rules.

Example:
```ttl
:liability06 a tosl:Liability ;
    dcterms:description """Neither OpenAI nor any of its affiliates or licensors will be liable for any indirect, incidental, special, consequential, or exemplary damages. The total liability is limited to the greater of: (1) the amount paid by the user in the prior 12 months for the specific service, or (2) $100. These limitations apply only to the maximum extent permitted by applicable law.""" ;
    tosl:liableParty :OpenAI ;
    tosl:targetParty :businessCustomer ;
    rdf:value tosl:anyIndirectDamage, tosl:anyLoss, tosl:legalCompliance ;
    tosl:limitation [
        a odrl:LogicalConstraint ;
        odrl:or (
            [
                a odrl:Constraint ;
                odrl:leftOperand tosl:totalAmount ;
                odrl:operator odrl:lte ;
                odrl:rightOperand :consumerQuote12Months
            ]
            [
                a odrl:Constraint ;
                odrl:leftOperand odrl:payAmount ;
                odrl:operator odrl:eq ;
                odrl:rightOperand "100.00"^^xsd:decimal ;
                odrl:unit <http://dbpedia.org/resource/United_States_dollar>
            ]
        )
    ] .

```
