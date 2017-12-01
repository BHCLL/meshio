# -*- coding: utf-8 -*-
#
import helpers

import pytest

import meshio

import legacy_reader

vtk = pytest.importorskip('vtk')


@pytest.mark.parametrize('mesh', [
        helpers.tri_mesh,
        helpers.triangle6_mesh,
        helpers.quad_mesh,
        helpers.quad8_mesh,
        helpers.tri_quad_mesh,
        helpers.tet_mesh,
        helpers.tet10_mesh,
        helpers.hex_mesh,
        helpers.hex20_mesh,
        helpers.add_point_data(helpers.tri_mesh, 1),
        helpers.add_point_data(helpers.tri_mesh, 2),
        helpers.add_point_data(helpers.tri_mesh, 3),
        helpers.add_cell_data(helpers.tri_mesh, 1),
        helpers.add_cell_data(helpers.tri_mesh, 2),
        helpers.add_cell_data(helpers.tri_mesh, 3),
        ])
def test_ascii(mesh):
    def writer(filename, points, cells, point_data, cell_data, field_data):
        return meshio.vtk_io.write(
            filename, points, cells, point_data, cell_data, field_data,
            write_binary=False
            )

    helpers.write_read2(writer, meshio.vtk_io.read, mesh, 1.0e-15)

    # test with legacy writer
    def legacy_writer(
            filename, points, cells, point_data, cell_data, field_data
            ):
        return meshio.legacy_writer.write(
            'vtk-ascii',
            filename, points, cells, point_data, cell_data, field_data
            )

    # The legacy writer only writes with low precision.
    helpers.write_read2(legacy_writer, meshio.vtk_io.read, mesh, 1.0e-11)

    # test with legacy reader
    # The legacy writer only writes with low precision.
    def lr(filename):
        return legacy_reader.read('vtk-ascii', filename)

    helpers.write_read2(writer, lr, mesh, 1.0e-15)
    return


@pytest.mark.parametrize('mesh', [
        helpers.tri_mesh,
        helpers.triangle6_mesh,
        helpers.quad_mesh,
        helpers.quad8_mesh,
        helpers.tri_quad_mesh,
        helpers.tet_mesh,
        helpers.tet10_mesh,
        helpers.hex_mesh,
        helpers.hex20_mesh,
        helpers.add_point_data(helpers.tri_mesh, 1),
        helpers.add_point_data(helpers.tri_mesh, 2),
        helpers.add_point_data(helpers.tri_mesh, 3),
        helpers.add_cell_data(helpers.tri_mesh, 1),
        helpers.add_cell_data(helpers.tri_mesh, 2),
        helpers.add_cell_data(helpers.tri_mesh, 3),
        ])
def test_binary(mesh):
    def writer(filename, points, cells, point_data, cell_data, field_data):
        return meshio.vtk_io.write(
            filename, points, cells, point_data, cell_data, field_data,
            write_binary=True
            )

    helpers.write_read2(writer, meshio.vtk_io.read, mesh, 1.0e-15)

    # test with legacy writer
    def legacy_writer(
            filename, points, cells, point_data, cell_data, field_data
            ):
        return meshio.legacy_writer.write(
            'vtk-binary',
            filename, points, cells, point_data, cell_data, field_data
            )

    # The legacy writer only writes with low precision.
    helpers.write_read2(legacy_writer, meshio.vtk_io.read, mesh, 1.0e-11)

    # test with legacy reader
    # The legacy writer only writes with low precision.
    def lr(filename):
        return legacy_reader.read('vtk-binary', filename)

    helpers.write_read2(writer, lr, mesh, 1.0e-15)
    return


if __name__ == '__main__':
    test_binary(helpers.tri_mesh)
