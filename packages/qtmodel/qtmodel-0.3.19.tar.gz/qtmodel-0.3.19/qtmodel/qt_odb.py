from __main__ import qt_model
from .res_db import *
from .qt_db import *


class Odb:
    """
    获取模型计算结果和模型信息
    """

    # region 静力结果查看
    @staticmethod
    def get_element_stress(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取单元应力,支持单个单元和单元列表
        Args:
            element_id: 单元编号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        example:
            odb.get_element_stress(1,stage_id=1)
            odb.get_element_stress([1,2,3],stage_id=1)
            odb.get_element_stress(1,stage_id=-1,case_name="工况名")
        Returns: list[ElementStress] or ElementStress
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,element_id仅支持 int和 list[int]")
        bf_list = qt_model.GetElementStress(element_id, stage_id, result_kind, increment_type, case_name)
        list_res = []
        for item in bf_list:
            if item.ElementType == "BEAM":
                stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                            item.StressI[6], item.StressI[7], item.StressI[8]]
                stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                            item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                list_res.append(BeamElementStress(item.ElementId, stress_i, stress_j))
            elif item.ElementType == "SHELL" or item.ElementType == "PLATE":
                stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4]]
                stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4]]
                stress_k = [item.StressK[0], item.StressK[1], item.StressK[2], item.StressK[3], item.StressK[4]]
                stress_l = [item.StressL[0], item.StressL[1], item.StressL[2], item.StressL[3], item.StressL[4]]
                stress_i2 = [item.StressI2[0], item.StressI2[1], item.StressI2[2], item.StressI2[3], item.StressI2[4]]
                stress_j2 = [item.StressJ2[0], item.StressJ2[1], item.StressJ2[2], item.StressJ2[3], item.StressJ2[4]]
                stress_k2 = [item.StressK2[0], item.StressK2[1], item.StressK2[2], item.StressK2[3], item.StressK2[4]]
                stress_l2 = [item.StressL2[0], item.StressL2[1], item.StressL2[2], item.StressL2[3], item.StressL2[4]]
                list_res.append(ShellElementStress(item.ElementId, stress_i, stress_j, stress_k, stress_l,
                                                   stress_i2, stress_j2, stress_k2, stress_l2))
            elif item.ElementType == "CABLE" or item.ElementType == "LINK" or item.ElementType == "TRUSS":
                stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                            item.StressI[6], item.StressI[7], item.StressI[8]]
                stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                            item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                list_res.append(TrussElementStress(item.ElementId, stress_i, stress_j))
            elif item.ElementType == "COM-BEAM":
                stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                            item.StressI[6], item.StressI[7], item.StressI[8]]
                stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                            item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                stress_i2 = [item.StressI2[0], item.StressI2[1], item.StressI2[2], item.StressI2[3], item.StressI2[4], item.StressI2[5],
                             item.StressI2[6], item.StressI2[7], item.StressI2[8]]
                stress_j2 = [item.StressJ2[0], item.StressJ2[1], item.StressJ2[2], item.StressJ2[3], item.StressJ2[4], item.StressJ2[5],
                             item.StressJ2[6], item.StressJ2[7], item.StressJ2[8]]
                list_res.append(CompositeBeamStress(element_id, stress_i, stress_j, stress_i2, stress_j2))
            else:
                raise TypeError(f"操作错误，不存在{item.ElementType}类型")
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_element_force(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取单元内力,支持单个单元和单元列表
        Args:
            element_id: 单元编号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        example:
            odb.get_element_force(1,stage_id=1)
            odb.get_element_force([1,2,3],stage_id=1)
            odb.get_element_force(1,stage_id=-1,case_name="工况名")
        Returns: list[ElementForce] or ElementForce
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,element_id仅支持 int和 list[int]")
        bf_list = qt_model.GetElementForce(element_id, stage_id, result_kind, increment_type, case_name)
        list_res = []
        for item in bf_list:
            if item.ElementType == "BEAM":
                force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                list_res.append(BeamElementForce(item.ElementId, force_i, force_j))
            elif item.ElementType == "SHELL" or item.ElementType == "PLATE":
                force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                force_k = [item.ForceK.Fx, item.ForceK.Fy, item.ForceK.Fz, item.ForceK.Mx, item.ForceK.My, item.ForceK.Mz]
                force_l = [item.ForceL.Fx, item.ForceL.Fy, item.ForceL.Fz, item.ForceL.Mx, item.ForceL.My, item.ForceL.Mz]
                list_res.append(ShellElementForce(item.ElementId, force_i, force_j, force_k, force_l))
            elif item.ElementType == "CABLE" or item.ElementType == "LINK" or item.ElementType == "TRUSS":
                force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                list_res.append(TrussElementForce(item.ElementId, force_i, force_j))
            elif item.ElementType == "COM-BEAM":
                all_force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                all_force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                main_force_i = [item.MainForceI.Fx, item.MainForceI.Fy, item.MainForceI.Fz, item.MainForceI.Mx, item.MainForceI.My,
                                item.MainForceI.Mz]
                main_force_j = [item.MainForceJ.Fx, item.MainForceJ.Fy, item.MainForceJ.Fz, item.MainForceJ.Mx, item.MainForceJ.My,
                                item.MainForceJ.Mz]
                sub_force_i = [item.SubForceI.Fx, item.SubForceI.Fy, item.SubForceI.Fz, item.SubForceI.Mx, item.SubForceI.My, item.SubForceI.Mz]
                sub_force_j = [item.SubForceJ.Fx, item.SubForceJ.Fy, item.SubForceJ.Fz, item.SubForceJ.Mx, item.SubForceJ.My, item.SubForceJ.Mz]
                is_composite = item.IsComposite
                shear_force = item.ShearForce
                list_res.append(CompositeElementForce(item.ElementId, all_force_i, all_force_j, shear_force,
                                                      main_force_i, main_force_j, sub_force_i, sub_force_j, is_composite))

            else:
                raise TypeError(f"操作错误，不存在{item.ElementType}类型")
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_reaction(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点编号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        example:
            odb.get_reaction(1,stage_id=1)
            odb.get_reaction([1,2,3],stage_id=1)
            odb.get_reaction(1,stage_id=-1,case_name="工况名")
        Returns: list[SupportReaction] or SupportReaction
        """
        if type(node_id) != int and type(node_id) != list:
            raise TypeError("类型错误,beam_id int和 list[int]")
        bs_list = qt_model.GetSupportReaction(node_id, stage_id, result_kind, increment_type, case_name)
        list_res = []
        for item in bs_list:
            force = [item.Force.Fx, item.Force.Fy, item.Force.Fz, item.Force.Mx, item.Force.My, item.Force.Mz]
            list_res.append(SupportReaction(item.NodeId, force))
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_node_displacement(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        example:
            odb.get_node_displacement(1,stage_id=1)
            odb.get_node_displacement([1,2,3],stage_id=1)
            odb.get_node_displacement(1,stage_id=-1,case_name="工况名")
        Returns: list[NodeDisplacement] or NodeDisplacement
        """
        if type(node_id) != int and type(node_id) != list:
            raise TypeError("类型错误,node_id仅支持 int和 list[int]")
        bf_list = qt_model.GetNodeDisplacement(node_id, stage_id, result_kind, increment_type, case_name)
        list_res = []
        for item in bf_list:
            displacements = [item.Displacement.Dx, item.Displacement.Dy, item.Displacement.Dz,
                             item.Displacement.Rx, item.Displacement.Ry, item.Displacement.Rz]
            list_res.append(NodeDisplacement(item.NodeId, displacements))
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    # endregion

    # region 绘制模型结果
    @staticmethod
    def plot_reaction_result(file_path: str, component: int = 1, load_case_name: str = "", stage_id: int = 1,
                             envelope_type: int = 1, show_number: bool = True, show_legend: bool = True,
                             text_rotation=0, digital_count=0, show_exponential: bool = True, max_min_kind: int = -1,
                             show_increment: bool = False):
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Fx 1-Fy 2-Fz 3-Fxyz 4-Mx 5-My 6-Mz 7-Mxyz
            load_case_name: 详细荷载工况名，参考桥通结果输出，例如： CQ:成桥(合计)
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            show_number: 数值选项卡开启
            show_legend: 图例选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            show_increment: 是否显示增量结果
        example:
            odb.plot_reaction_result(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        qt_model.PlotReactionResult(file_path, component=component, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
                                    showNumber=show_number, showLegend=show_legend, textRotationAngle=text_rotation, digitalCount=digital_count,
                                    showAsExponential=show_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)

    @staticmethod
    def plot_displacement_result(file_path: str, component: int = 1, load_case_name: str = "", stage_id: int = 1,
                                 envelope_type: int = 1, show_deformed: bool = True, show_pre_deformed: bool = True,
                                 deformed_scale: float = 1.0, actual_deformed: bool = False,
                                 show_number: bool = True, show_legend: bool = True,
                                 text_rotation=0, digital_count=0, show_exponential: bool = True, max_min_kind: int = 1,
                                 show_increment: bool = False):
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Dx 1-Dy 2-Dz 3-Rx 4-Ry 5-Rz 6-Dxy 7-Dyz 8-Dxz 9-Dxyz
            load_case_name: 详细荷载工况名，参考桥通结果输出，例如： CQ:成桥(合计)
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            show_deformed: 变形选项卡开启
            show_pre_deformed: 显示变形前
            deformed_scale:变形比例
            actual_deformed:是否显示实际变形
            show_number: 数值选项卡开启
            show_legend: 图例选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            show_increment: 是否显示增量结果
        example:
            odb.plot_displacement_result(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        qt_model.PlotDisplacementResult(file_path, component=component, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
                                        showAsDeformedShape=show_deformed, showUndeformedShape=show_pre_deformed,
                                        deformedScale=deformed_scale, deformedActual=actual_deformed,
                                        showNumber=show_number, showLegend=show_legend, textRotationAngle=text_rotation, digitalCount=digital_count,
                                        showAsExponential=show_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)

    @staticmethod
    def plot_beam_element_force(file_path: str, component: int = 0, load_case_name: str = "合计", stage_id: int = 1,
                                envelope_type: int = 1, show_line_chart: bool = True, show_number: bool = False,
                                position: int = 0, flip_plot: bool = True, line_scale: float = 1.0,
                                show_deformed: bool = True, show_pre_deformed: bool = False,
                                deformed_actual: bool = False, deformed_scale: float = 1.0,
                                show_legend: bool = True, text_rotation: int = 0, digital_count: int = 0,
                                show_exponential: bool = True, max_min_kind: int = 0, show_increment: bool = False):
        """
        绘制梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Fx 1-Fy 2-Fz 3-Mx 4-My 5-Mz
            load_case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelope_type: 包络类型
            show_line_chart: 是否显示线图
            show_number: 是否显示数值
            position: 位置编号
            flip_plot: 是否翻转绘图
            line_scale: 线的比例
            show_deformed: 是否显示变形形状
            show_pre_deformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
        example:
            odb.plot_beam_element_force(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        qt_model.PlotBeamElementForce(
            filePath=file_path, component=component, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
            showLineChart=show_line_chart, showNumber=show_number, position=position, flipPlot=flip_plot, lineScale=line_scale,
            showAsDeformedShape=show_deformed, showUndeformedShape=show_pre_deformed, deformedActual=deformed_actual,
            deformedScale=deformed_scale, showLegend=show_legend, textRotationAngle=text_rotation, digitalCount=digital_count,
            showAsExponential=show_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)

    @staticmethod
    def plot_truss_element_force(file_path: str, load_case_name: str = "合计", stage_id: int = 1,
                                 envelope_type: int = 1, show_line_chart: bool = True, show_number: bool = False,
                                 position: int = 0, flip_plot: bool = True, line_scale: float = 1.0,
                                 show_deformed: bool = True, show_pre_deformed: bool = False,
                                 deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_legend: bool = True, text_rotation_angle: int = 0, digital_count: int = 0,
                                 show_as_exponential: bool = True, max_min_kind: int = 0, show_increment: bool = False):
        """
        绘制杆单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            load_case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelope_type: 包络类型
            show_line_chart: 是否显示线图
            show_number: 是否显示数值
            position: 位置编号
            flip_plot: 是否翻转绘图
            line_scale: 线的比例
            show_deformed: 是否显示变形形状
            show_pre_deformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotation_angle: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_as_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment:是否显示增量结果
        example:
            odb.plot_truss_element_force(r"aaa.png",load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        qt_model.PlotTrussElementForce(
            filePath=file_path, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
            showLineChart=show_line_chart, showNumber=show_number, position=position, flipPlot=flip_plot, lineScale=line_scale,
            showAsDeformedShape=show_deformed, showUndeformedShape=show_pre_deformed, deformedActual=deformed_actual,
            deformedScale=deformed_scale, showLegend=show_legend, textRotationAngle=text_rotation_angle, digitalCount=digital_count,
            showAsExponential=show_as_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)

    @staticmethod
    def plot_plate_element_force(file_path: str, component: int = 0, force_kind: int = 0, load_case_name: str = "合计",
                                 stage_id: int = 1, envelope_type: int = 1, show_number: bool = False,
                                 show_deformed: bool = True, show_pre_deformed: bool = False,
                                 deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_legend: bool = True, text_rotation_angle: int = 0, digital_count: int = 0,
                                 show_as_exponential: bool = True, max_min_kind: int = 0, show_increment: bool = False):
        """
        绘制板单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Fxx 1-Fyy 2-Fxy 3-Mxx 4-Myy 5-Mxy
            force_kind: 力类型
            load_case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelope_type: 包络类型
            show_number: 是否显示数值
            show_deformed: 是否显示变形形状
            show_pre_deformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotation_angle: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_as_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
        example:
            odb.plot_plate_element_force(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        qt_model.PlotPlateElementForce(
            filePath=file_path, component=component, forceKind=force_kind, loadCaseName=load_case_name, stageId=stage_id,
            envelopeType=envelope_type, showNumber=show_number, showAsDeformedShape=show_deformed,
            showUndeformedShape=show_pre_deformed, deformedActual=deformed_actual, deformedScale=deformed_scale,
            showLegend=show_legend, textRotationAngle=text_rotation_angle, digitalCount=digital_count,
            showAsExponential=show_as_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)

    # endregion

    # region 获取模型信息
    @staticmethod
    def get_section_data(sec_id: int):
        """
        获取截面详细信息
        Args:
            sec_id: 目标截面编号
        example:
            odb.get_node_id(1,1,1)
        Returns: int
        """
        return qt_model.GetSectionInfo(sec_id)

    @staticmethod
    def get_node_id(x: float = 0, y: float = 0, z: float = 0, tolerance: float = 1e-4):
        """
        获取节点编号，为-1时则表示未找到该坐标节点
        Args:
            x: 目标点X轴坐标
            y: 目标点Y轴坐标
            z: 目标点Z轴坐标
            tolerance: 距离容许误差
        example:
            odb.get_node_id(1,1,1)
        Returns: int
        """
        return qt_model.GetNodeId(x=x, y=y, z=z, tolerance=tolerance)

    @staticmethod
    def get_group_elements(group_name: str = "默认结构组"):
        """
        获取结构组单元编号
        Args:
            group_name: 结构组名
        example:
            odb.get_group_elements("默认结构组")
        Returns: list[int]
        """
        return list(qt_model.GetStructureGroupElements(group_name))

    @staticmethod
    def get_group_nodes(group_name: str = "默认结构组"):
        """
        获取结构组节点编号
        Args:
            group_name: 结构组名
        example:
            odb.get_group_nodes("默认结构组")
        Returns: list[int]
        """
        return list(qt_model.GetStructureGroupNodes(group_name))

    @staticmethod
    def get_node_data(ids=None):
        """
        获取节点信息 默认获取所有节点信息
        Args: 无
        example:
            odb.get_node_data()     # 获取所有节点信息
            odb.get_node_data(1)    # 获取单个节点信息
            odb.get_node_data([1,2])    # 获取多个节点信息
        Returns: list[Node] 或 Node
        """
        if ids is None:
            node_list = qt_model.GetNodeData()
        else:
            node_list = qt_model.GetNodeData(ids)
        res_list = []
        for item in node_list:
            res_list.append(Node(item.Id, item.XCoor, item.YCoor, item.ZCoor))
        if len(res_list) == 1:
            return res_list[0]
        return res_list

    @staticmethod
    def get_element_data(ids=None):
        """
        获取单元信息
        Args: 无
        example:
            odb.get_element_data() # 获取所有单元结果
            odb.get_element_data(1) # 获取指定编号单元信息
        Returns: list[Element]
        """
        ele_list = []
        target_ids = []
        if ids is None:
            ele_list.extend(Odb.get_beam_element())
            ele_list.extend(Odb.get_plate_element())
            ele_list.extend(Odb.get_cable_element())
            ele_list.extend(Odb.get_link_element())
            if len(ele_list) == 1:
                return ele_list[0]
            else:
                return ele_list
        if isinstance(ids, int):
            target_ids.append(ids)
        else:
            target_ids.extend(ids)
        for item_id in target_ids:
            ele_type = Odb.get_element_type(item_id)
            if ele_type == "BEAM":
                ele_list.append(Odb.get_beam_element(item_id)[0])
            if ele_type == "PLATE":
                ele_list.append(Odb.get_plate_element(item_id)[0])
            if ele_type == "CABLE":
                ele_list.append(Odb.get_cable_element(item_id)[0])
            if ele_type == "LINK":
                ele_list.append(Odb.get_link_element(item_id)[0])
        return ele_list

    @staticmethod
    def get_element_type(ele_id: int) -> str:
        """
        获取单元类型
        Args:
            ele_id: 单元号
        example:
            odb.get_element_type(1) # 获取所有单元信息
        Returns: str类型 返回 BEAM PLATE CABLE LINK
        """
        return qt_model.GetElementType(ele_id)

    @staticmethod
    def get_beam_element(ids=None) -> list[Element]:
        """
        获取梁单元信息
        Args:
            ids: 梁单元号，默认时获取所有梁单元
        example:
            odb.get_beam_element() # 获取所有单元信息
        Returns: list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetBeamElementData()
        else:
            ele_list = qt_model.GetBeamElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "BEAM", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle))
        return res_list

    @staticmethod
    def get_plate_element(ids=None) -> list[Element]:
        """
        获取板单元信息
        Args:
            ids: 板单元号，默认时获取所有板单元
        example:
            odb.get_plate_element() # 获取所有单元信息
        Returns: list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetPlateElementData()
        else:
            ele_list = qt_model.GetPlateElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "PLATE", [item.NodeI.Id, item.NodeJ.Id, item.NodeK.Id, item.NodeL.Id],
                                    item.MaterialId, item.ThicknessId, item.BetaAngle))
        return res_list

    @staticmethod
    def get_cable_element(ids=None) -> list[Element]:
        """
        获取索单元信息
        Args:
            ids: 索单元号，默认时获取所有索单元
        example:
            odb.get_cable_element() # 获取所有单元信息
        Returns: list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetCableElementData()
        else:
            ele_list = qt_model.GetCableElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "CABLE", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle,
                                    int(item.InitialParameterType), item.InitialParameter))
        return res_list

    @staticmethod
    def get_link_element(ids=None) -> list[Element]:
        """
        获取杆单元信息
        Args:
            ids: 杆单元号，默认时输出全部杆单元
        example:
            odb.get_link_element() # 获取所有单元信息
        Returns: list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetLinkElementData()
        else:
            ele_list = qt_model.GetLinkElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "LINK", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle))
        return res_list

    @staticmethod
    def get_material_data(ids=None):
        """
        获取材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        example:
            odb.get_material_data() # 获取所有材料信息
        Returns: list[Material]
        """
        mat_list = []
        # if ids is None:
        #     mat_list.extend(qt_model.GetConcreteMaterialData())
        #     mat_list.extend(qt_model.GeSteelPlateMaterialData())
        #     mat_list.extend(qt_model.GetSteelBarMaterialData())
        #     mat_list.extend(qt_model.GetPreStressedBarMaterialData())
        #     mat_list.extend(qt_model.GetUserDefinedMaterialData())

    @staticmethod
    def get_concrete_material(ids=None) -> list[Material]:
        """
        获取混凝土材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        example:
            odb.get_concrete_material() # 获取所有材料信息
        Returns: list[Material]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetConcreteMaterialData()
        else:
            ele_list = qt_model.GetConcreteMaterialData(ids)
        for item in ele_list:
            res_list.append(Material(item.Id, item.Name, "混凝土", item.Standard, item.Database,
                                     [item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                     item.Standard, item.IsModifiedByUser))
        return res_list
    # endregion
