import logging
import sys
import unittest
from pathlib import Path

from rdflib import OWL, RDF, RDFS, SH, XSD, BNode, Graph, Literal, Namespace
from rdflib.compare import isomorphic
from rdflib.term import URIRef

from shacltool.owl2shacl import create_shacl, rdf_validate

IES = Namespace("http://ies.data.gov.uk/ontology/ies4#")
DATA = Namespace("http://data.gov.uk/testdata#")
ISO8601 = Namespace("http://iso.org/iso8601#")
SPARX = Namespace("http://data.sparxsystems.com#")
SH_CLASS = URIRef("http://www.w3.org/ns/shacl#class")
SH_OR = URIRef("http://www.w3.org/ns/shacl#or")

logging.basicConfig(stream=sys.stdout, level=logging.INFO, force=True)


class TestOwl2Shacl(unittest.TestCase):
    @unittest.skip("failing with missing file, please fix.")
    def test_valid_data(self):
        expected_result = Graph()
        vrep = BNode()
        expected_result.add((vrep, RDF.type, SH.ValidationReport))
        expected_result.add((vrep, SH.conforms, Literal("true", datatype=XSD.boolean)))
        # ont_file = Path("IES Specification Docs/Information Exchange Standard r4.2.0.n3")
        __root = Path(__file__).absolute().parent.parent

        ont_file = __root / "IES Specification Docs/IES4.ttl"
        ont_graph, sh_graph = create_shacl(ont_file)
        conforms, results_graph, results_text = rdf_validate(
            "Sample Data/hospital.ttl", ont_graph, sh_graph)
        self.assertTrue(conforms)
        self.assertEqual("Validation Report\nConforms: True\n", results_text)
        assert isomorphic(expected_result, results_graph)

    # @unittest.skip("done")
    def test_object_property_not_class(self):
        expected_result = Graph()
        vrep = BNode()
        vres = BNode()
        expected_result.add((vrep, RDF.type, SH.ValidationReport))
        expected_result.add((vrep, SH.conforms, Literal("false", datatype=XSD.boolean)))
        expected_result.add((vrep, SH.result, vres))
        expected_result.add((vres, RDF.type, SH.ValidationResult))
        expected_result.add((vres, SH.focusNode, Literal("Fred")))
        expected_result.add((vres, SH.resultMessage, Literal("Value does not have class ies:Name")))
        expected_result.add((vres, SH.resultSeverity, SH.Warning))
        expected_result.add((vres, SH.sourceConstraintComponent, SH.ClassConstraintComponent))
        expected_result.add((vres, SH.sourceShape, IES.HasNameRangeShape))
        expected_result.add((vres, SH.value, Literal("Fred")))

        data_graph = Graph()
        data_graph.bind('ies', IES)
        data_graph.bind('data', DATA)
        data_graph.add((DATA.Fred, RDF.type, IES.Person))
        data_graph.add((DATA.Fred, IES.hasName, Literal("Fred")))

        ont_file = Path("IES Specification Docs/Information Exchange Standard r4.2.0.n3")

        ont_graph, sh_graph = create_shacl(ont_file)
        conforms, results_graph, results_text = rdf_validate(data_graph, ont_graph, sh_graph)
        logging.info(results_graph.serialize(format="turtle"))
        self.assertFalse(conforms)
        assert isomorphic(expected_result, results_graph)

    # @unittest.skip("done")
    def test_object_property_superclass(self):
        expected_result = Graph()
        vrep = BNode()
        vres = BNode()
        expected_result.add((vrep, RDF.type, SH.ValidationReport))
        expected_result.add((vrep, SH.conforms, Literal("false", datatype=XSD.boolean)))
        expected_result.add((vrep, SH.result, vres))
        expected_result.add((vres, RDF.type, SH.ValidationResult))
        expected_result.add((vres, SH.focusNode, DATA.John))
        expected_result.add((vres, SH.resultMessage, Literal("Value does not have class ies:Person")))
        expected_result.add((vres, SH.resultSeverity, SH.Warning))
        expected_result.add((vres, SH.sourceConstraintComponent, SH.ClassConstraintComponent))
        expected_result.add((vres, SH.sourceShape, IES.SiblingOfRangeShape))
        expected_result.add((vres, SH.value, DATA.John))

        data_graph = Graph()
        data_graph.bind('ies', IES)
        data_graph.bind('data', DATA)
        data_graph.add((DATA.Fred, RDF.type, IES.Person))
        data_graph.add((DATA.Fred, IES.hasName, DATA.fredName))
        data_graph.add((DATA.fredName, RDF.type, IES.Name))
        data_graph.add((DATA.Fred, IES.siblingOf, DATA.John))
        data_graph.add((DATA.John, RDF.type, IES.ResponsibleActor))

        ont_file = Path("IES Specification Docs/Information Exchange Standard r4.2.0.n3")

        ont_graph, sh_graph = create_shacl(ont_file)
        conforms, results_graph, results_text = rdf_validate(data_graph, ont_graph, sh_graph)
        res = results_graph.serialize(format="turtle")
        logging.info(res)
        self.assertFalse(conforms)
        assert isomorphic(expected_result, results_graph)

    # @unittest.skip("done")
    def test_object_property_invalid_class(self):
        expected_result = Graph()
        vrep = BNode()
        vres = BNode()
        expected_result.add((vrep, RDF.type, SH.ValidationReport))
        expected_result.add((vrep, SH.conforms, Literal("false", datatype=XSD.boolean)))
        expected_result.add((vrep, SH.result, vres))
        expected_result.add((vres, RDF.type, SH.ValidationResult))
        expected_result.add((vres, SH.focusNode, DATA.fredName))
        expected_result.add((vres, SH.resultMessage, Literal("Value does not have class ies:Name")))
        expected_result.add((vres, SH.resultSeverity, SH.Warning))
        expected_result.add((vres, SH.sourceConstraintComponent, SH.ClassConstraintComponent))
        expected_result.add((vres, SH.sourceShape, IES.HasNameRangeShape))
        expected_result.add((vres, SH.value, DATA.fredName))

        data_graph = Graph()
        data_graph.bind('ies', IES)
        data_graph.bind('data', DATA)
        data_graph.add((DATA.Fred, RDF.type, IES.Person))
        data_graph.add((DATA.Fred, IES.hasName, DATA.fredName))
        data_graph.add((DATA.fredName, RDF.type, IES.Location))

        ont_file = Path("IES Specification Docs/Information Exchange Standard r4.2.0.n3")

        ont_graph, sh_graph = create_shacl(ont_file)
        conforms, results_graph, results_text = rdf_validate(data_graph, ont_graph, sh_graph)
        res = results_graph.serialize(format="turtle")
        logging.info(res)
        self.assertFalse(conforms)
        assert isomorphic(expected_result, results_graph)

    # @unittest.skip("done")
    def test_object_property_not_all_specified_classes(self):
        expected_result = Graph()
        vrep = BNode()
        vres = BNode()
        vres2 = BNode()
        expected_result.add((vrep, RDF.type, SH.ValidationReport))
        expected_result.add((vrep, SH.conforms, Literal("false", datatype=XSD.boolean)))
        expected_result.add((vrep, SH.result, vres))
        expected_result.add((vrep, SH.result, vres2))
        expected_result.add((vres, RDF.type, SH.ValidationResult))
        expected_result.add((vres, SH.focusNode, DATA.TravelTicket))
        msg = "Value class is not in classes (ies:IdentityDocument, ies:PaymentArtefact, ies:TravelTicket)"
        expected_result.add((vres, SH.resultMessage, Literal(msg)))
        expected_result.add((vres, SH.resultSeverity, SH.Warning))
        expected_result.add((vres, SH.sourceConstraintComponent, SH.ClassConstraintComponent))
        expected_result.add((vres, SH.sourceShape, IES.ValidFromDateDomainShape))
        expected_result.add((vres, SH.value, DATA.TravelTicket))
        expected_result.add((vres2, RDF.type, SH.ValidationResult))
        expected_result.add((vres2, SH.focusNode, DATA.TravelTicket))
        msg1 = "Value class is not in classes (ies:IdentityDocument, ies:PaymentArtefact, ies:TravelTicket)"
        expected_result.add((vres2, SH.resultMessage, Literal(msg1)))
        expected_result.add((vres2, SH.resultSeverity, SH.Warning))
        expected_result.add((vres2, SH.sourceConstraintComponent, SH.ClassConstraintComponent))
        expected_result.add((vres2, SH.sourceShape, IES.ValidFromDateDomainShape))
        expected_result.add((vres2, SH.value, DATA.TravelTicket))

        data_graph = Graph()
        data_graph.bind('ies', IES)
        data_graph.bind('data', DATA)
        data_graph.bind('iso8601', ISO8601)
        data_graph.add((DATA.TravelTicket, RDF.type, IES.TravelTicket))
        data_graph.add((DATA.TravelTicket, IES.validFromDate, URIRef(ISO8601 + "2014-01-04")))
        data_graph.add((URIRef(ISO8601 + "2014-01-04"), RDF.type, IES.ParticularPeriod))

        ont_file = Path("IES Specification Docs/Information Exchange Standard r4.2.0.n3")

        ont_graph, sh_graph = create_shacl(ont_file)
        conforms, results_graph, results_text = rdf_validate(data_graph, ont_graph, sh_graph)
        logging.info(results_graph.serialize(format="turtle"))
        self.assertFalse(conforms)
        assert isomorphic(expected_result, results_graph)

    # @unittest.skip("done")
    def test_object_property_one_of_specified_classes(self):
        expected_result = Graph()
        expected_result.bind('ies', IES)
        bn1 = BNode()
        bn2 = BNode()
        bn3 = BNode()
        bn4 = BNode()
        bn5 = BNode()
        bn6 = BNode()
        expected_result.add((IES.ValidFromDateRangeShape, RDF.type, SH.NodeShape))
        expected_result.add(
            (IES.ValidFromDateRangeShape, SH_CLASS, IES.ParticularPeriod))
        expected_result.add((IES.ValidFromDateRangeShape, SH.severity, SH.Warning))
        expected_result.add((IES.ValidFromDateRangeShape, SH.targetObjectsOf, IES.validFromDate))

        expected_result.add((IES.ValidFromDateDomainShape, RDF.type, SH.NodeShape))
        expected_result.add((IES.ValidFromDateDomainShape, SH_OR, bn1))
        expected_result.add((bn1, RDF.first, bn2))
        expected_result.add((bn1, RDF.rest, bn3))
        expected_result.add((bn3, RDF.first, bn4))
        expected_result.add((bn3, RDF.rest, bn5))
        expected_result.add((bn5, RDF.first, bn6))
        expected_result.add((bn5, RDF.rest, RDF.nil))
        expected_result.add((bn2, SH_CLASS, IES.IdentityDocument))
        expected_result.add((bn4, SH_CLASS, IES.PaymentArtefact))
        expected_result.add((bn6, SH_CLASS, IES.TravelTicket))
        expected_result.add((IES.ValidFromDateDomainShape, SH.severity, SH.Warning))
        expected_result.add((IES.ValidFromDateDomainShape, SH.targetSubjectsOf, IES.validFromDate))

        ont_graph = Graph()
        ont_graph.bind('ies', IES)
        ont_graph.bind('sparx', SPARX)
        dom = BNode()
        cls1 = BNode()
        cls2 = BNode()
        cls3 = BNode()

        ont_graph.add((IES.validFromDate, RDF.type, OWL.ObjectProperty))
        ont_graph.add((IES.validFromDate, SPARX.guid, Literal("{6ACC2ACC-46F2-4a02-A3E7-D16BE8EB723B}")))
        ont_graph.add((IES.validFromDate, RDFS.comment,
                       Literal("The date that the respective IdentityDocument or Ticket is valid from.")))
        ont_graph.add((IES.validFromDate, RDFS.subPropertyOf, IES.relationship))
        ont_graph.add((IES.validFromDate, RDFS.range, IES.ParticularPeriod))
        ont_graph.add((IES.validFromDate, RDFS.domain, dom))
        ont_graph.add((dom, RDF.type, OWL.Class))
        ont_graph.add((dom, OWL.unionOf, cls1))
        ont_graph.add((cls1, RDF.first, IES.IdentityDocument))
        ont_graph.add((cls1, RDF.rest, cls2))
        ont_graph.add((cls2, RDF.first, IES.PaymentArtefact))
        ont_graph.add((cls2, RDF.rest, cls3))
        ont_graph.add((cls3, RDF.first, IES.TravelTicket))
        ont_graph.add((cls3, RDF.rest, RDF.nil))

        new_ont_graph, sh_graph = create_shacl(ont_graph)
        logging.info(ont_graph.serialize(format="turtle"))
        logging.info(expected_result.serialize(format="turtle"))
        logging.info(sh_graph.serialize(format="turtle"))
        assert isomorphic(expected_result, sh_graph)

    # @unittest.skip("done")
    def test_datatype_property_one_of_specified_range(self):
        expected_result = Graph()
        expected_result.bind('ies', IES)
        bn1 = BNode()
        bn2 = BNode()
        bn3 = BNode()
        bn4 = BNode()
        bn5 = BNode()
        bn6 = BNode()
        expected_result.add((IES.TestPropertyRangeShape, RDF.type, SH.NodeShape))
        expected_result.add((IES.TestPropertyRangeShape, SH_OR, bn1))
        expected_result.add((bn1, RDF.first, bn2))
        expected_result.add((bn1, RDF.rest, bn3))
        expected_result.add((bn3, RDF.first, bn4))
        expected_result.add((bn3, RDF.rest, bn5))
        expected_result.add((bn5, RDF.first, bn6))
        expected_result.add((bn5, RDF.rest, RDF.nil))
        expected_result.add((bn2, SH.datatype, XSD.boolean))
        expected_result.add((bn4, SH.datatype, XSD.date))
        expected_result.add((bn6, SH.datatype, XSD.integer))
        expected_result.add((IES.TestPropertyRangeShape, SH.severity, SH.Warning))
        expected_result.add((IES.TestPropertyRangeShape, SH.targetObjectsOf, IES.testProperty))

        expected_result.add((IES.TestPropertyDomainShape, RDF.type, SH.NodeShape))
        expected_result.add(
            (IES.TestPropertyDomainShape, SH_CLASS, IES.TestItem))
        expected_result.add((IES.TestPropertyDomainShape, SH.severity, SH.Warning))
        expected_result.add((IES.TestPropertyDomainShape, SH.targetSubjectsOf, IES.testProperty))

        ont_graph = Graph()
        ont_graph.bind('ies', IES)
        ont_graph.bind('sparx', SPARX)
        dom = BNode()
        dt1 = BNode()
        dt2 = BNode()
        dt3 = BNode()

        ont_graph.add((IES.testProperty, RDF.type, OWL.DatatypeProperty))
        ont_graph.add((IES.testProperty, SPARX.guid, Literal("{6ACC2ACC-46F2-4a02-A3E7-D16BE8EB723B}")))
        ont_graph.add((IES.testProperty, RDFS.comment,
                       Literal("Test property")))
        ont_graph.add((IES.testProperty, RDFS.subPropertyOf, IES.property))
        ont_graph.add((IES.testProperty, RDFS.domain, IES.TestItem))
        ont_graph.add((IES.testProperty, RDFS.range, dom))
        ont_graph.add((dom, RDF.type, RDFS.Datatype))
        ont_graph.add((dom, OWL.unionOf, dt1))
        ont_graph.add((dt1, RDF.first, XSD.boolean))
        ont_graph.add((dt1, RDF.rest, dt2))
        ont_graph.add((dt2, RDF.first, XSD.date))
        ont_graph.add((dt2, RDF.rest, dt3))
        ont_graph.add((dt3, RDF.first, XSD.integer))
        ont_graph.add((dt3, RDF.rest, RDF.nil))

        new_ont_graph, sh_graph = create_shacl(ont_graph)
        logging.info(ont_graph.serialize(format="turtle"))
        logging.info(expected_result.serialize(format="turtle"))
        logging.info(sh_graph.serialize(format="turtle"))
        assert isomorphic(expected_result, sh_graph)

    # @unittest.skip("done")
    def test_class_shapes(self):
        expected_result = Graph().parse('test/expected_results/test_class_shapes.ttl')
        ont_file = Path("test/TestOntology.ttl")
        new_ont_graph, sh_graph = create_shacl(ont_file)
        logging.info(expected_result.serialize(format="turtle"))
        logging.info(sh_graph.serialize(format="turtle"))
        assert isomorphic(expected_result, sh_graph)


if __name__ == '__main__':
    unittest.main()
