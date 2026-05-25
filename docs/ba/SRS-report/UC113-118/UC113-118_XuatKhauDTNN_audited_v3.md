# UC Readiness Review
**Functional / Black-box Test Readiness Template**

**Tài liệu:** UC113-118_XuatKhauDTNN.md (phiên bản 1.1)
**Ngày tạo:** 2026-05-07
**Tác giả:** QC Auditor Agent (Deep Re-audit v3)
**Phiên bản report:** v3

---

## Feature Brief

Chức năng Báo cáo tình hình xuất khẩu của tổ chức kinh tế có vốn ĐTNN (Mẫu A.IV.8b) dành cho Cục Hải quan / Bộ Tài chính trên Admin Site. Đây là báo cáo **chi tiết theo từng doanh nghiệp FDI** với bảng dữ liệu ĐỘNG (dynamic rows — thêm/xóa dòng). Hệ thống hỗ trợ 2 chế độ nhập liệu:

- **Chế độ A (Thủ công / Manual):** Người dùng nhập MST, hệ thống gọi API CSDL Đăng ký KD để auto-fill thông tin doanh nghiệp (Ngày cấp, Tên DN, Tỉnh/TP). Nếu không tìm thấy MST trong CSDL, các trường chuyển sang Enabled để nhập tay.
- **Chế độ B (API Hải quan):** Hệ thống quét toàn bộ tờ khai xuất khẩu đã thông quan, lọc MST thuộc danh sách FDI, SUM giá trị xuất khẩu theo từng MST và điền tự động vào bảng.

Bảng dữ liệu gồm 6 cột: STT, Mã số thuế, Ngày cấp, Tên doanh nghiệp, Tỉnh/TP, Xuất khẩu kỳ báo cáo (USD). Dòng Tổng cộng cập nhật real-time theo SUM(C6). Dữ liệu từ mẫu 8b là **nguồn tổng hợp xuất khẩu** cho Mẫu A.IV.8a (UC107-112). Kỳ báo cáo: Định kỳ năm. Giao diện: Periodic-single. Mã báo cáo: DTNN_A4_8B_[ID].

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| **80 / 110 raw → 72.7 / 100** | CONDITIONALLY READY |

**Lý do:** Tài liệu SRS v1.1 đã bổ sung AC, NFR, Pre/Post-conditions nhưng vẫn còn nhiều chi tiết chưa được làm rõ liên quan đến: chuyển đổi Mode A/B, decimal precision, max rows, empty table submit, và phân loại dữ liệu (free text vs dropdown) cho một số cột.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC113-118 | Báo cáo tình hình xuất khẩu của TCKT có vốn ĐTNN (Mẫu A.IV.8b) | v1.1 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.le2 | N/A | 2026-04-24 | 2026-05-06 |

| Mẫu biểu | Loại báo cáo | Phạm vi | Hình thức nộp |
|-----------|-------------|---------|---------------|
| Mẫu A.IV.8b | Định kỳ năm | Không có phạm vi | Báo cáo đơn lẻ (Single report form) |

| Cơ quan nhận | Đối tượng lập | Giao diện | Quy tắc sinh mã |
|-------------|--------------|-----------|-----------------|
| Cục Đầu tư nước ngoài, Bộ Tài chính | Cục Hải quan / Bộ Tài chính | Admin site | DTNN_A4_8B_[ID] |

**Đánh giá:** 5/5 — Clear. Thông tin định danh đầy đủ. Lưu ý: SRS ghi "DTNN_A4_8B_[ID]" nhưng theo CMR_09, tiền tố phân hệ là "FDI" (không phải "DTNN"). Cần xác nhận lại.

---
## 1. Objective & Scope

### 1.1 Objective
Hỗ trợ Cục Hải quan / Bộ Tài chính nộp báo cáo xuất khẩu trực tuyến theo từng doanh nghiệp FDI. Dữ liệu từ báo cáo này là nguồn tổng hợp xuất khẩu cho Mẫu 8a (UC107-112).

### 1.2 In Scope
- UC113-118.1: Xem danh sách báo cáo (nhóm theo kỳ hạn năm)
- UC113-118.2: Lập báo cáo (tạo mới) — Mode A (thủ công) và Mode B (API Hải quan)
- UC113-118.3: Các tác vụ bổ trợ (Xem chi tiết, Xem vòng đời, In, Export, Nộp, Chỉnh sửa, Xóa)

### 1.3 Out of Scope
- Không cho phép nộp báo cáo trễ hạn.
- Việc duyệt báo cáo được thực hiện ở UC riêng biệt.

**Đánh giá:** 4/5 — Partial.
**Lý do trừ điểm:** SRS ghi rõ Out of Scope không nộp trễ hạn, nhưng thiếu mô tả cụ thể: khi qua kỳ báo cáo ("Qua kỳ báo cáo"), nếu báo cáo đang ở trạng thái "Lưu nháp" thì có được tiếp tục chỉnh sửa/nộp hay không? CMR_04 chỉ quy định ẩn nút [Lập báo cáo] và [Import], nhưng không đề cập đến hành động trên bản ghi đã tồn tại.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Cục Hải quan | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo xuất khẩu. Tham chiếu: CMR_02 |
| Bộ Tài chính | Primary | Lập, nộp, chỉnh sửa, xóa báo cáo xuất khẩu. Tham chiếu: CMR_02 |
| Cục ĐTNN | Receiver | Nhận thông báo khi báo cáo được nộp thành công |
| Hệ thống | System | Tự động tính toán SUM, gọi API, gửi Notification, ghi Audit log |

**Đánh giá:** 7/10 — Partial.
**Lý do trừ điểm:**
- SRS tham chiếu CMR_02 (ĐTRNN — nhiều NĐT cùng quyền), nhưng đối tượng lập là cơ quan nhà nước (Cục Hải quan / Bộ Tài chính), không phải NĐT trong dự án. Mô hình phân quyền CMR_02 được thiết kế cho NĐT, không phù hợp với cơ quan nhà nước. Cần xác nhận: Cơ quan nhà nước áp dụng mô hình phân quyền nào? Mỗi cơ quan chỉ có 1 tài khoản lập báo cáo hay nhiều?
- Thiếu làm rõ: Nhiều người dùng cùng 1 cơ quan có thể đồng thời chỉnh sửa cùng 1 báo cáo không? Nếu có, áp dụng Last Write Wins như CMR_02?

---
<!-- PLACEHOLDER_S3 -->
